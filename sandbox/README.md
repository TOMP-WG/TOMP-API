# TOMP-API Sandbox

A small Node/Express server that simulates the **current v2 TOMP-API** (the `package`/`leg`,
OGC Processes/Collections-styled spec in `../TOMP-API.yaml`) for integration testing.

Unlike a static mock, this sandbox **really registers what you create**: calling
`purchase-offers` creates a persisted `package` record with a real id, and subsequent calls
(`confirm-purchase`, `start-leg`, `end-leg`, `confirm-payment`, ...) genuinely mutate that
record's state. Re-reading a package later reflects every change you made to it. State only
progresses when you call the next endpoint yourself (no automatic/time-based simulation).

Every request is validated against the real `../TOMP-API.yaml` spec via
`express-openapi-validator`, so this doubles as a contract check for client integrations.

## Run it

```bash
npm install
npm start        # listens on :4010 (set PORT to override)
npm run dev      # same, restarts on file changes
npm test         # automated lifecycle + error-path tests (supertest)
```

Copy `.env.example` to `.env` to override defaults (JWT secret, port, strict client-credential
checking). See that file for details.

## Postman collection

`postman/TOMP-API-Sandbox.postman_collection.json` drives the whole lifecycle through Postman (or
`newman`, Postman's CLI runner). It's self-contained - no separate environment file needed, all
variables (`baseUrl`, `clientId`/`clientSecret`, and the ids captured along the way) are built into
the collection with sensible defaults for a locally running sandbox.

- **Import** it into Postman, or run it headless:
  ```bash
  npx newman run postman/TOMP-API-Sandbox.postman_collection.json
  ```
- **Folders run in order** (00 → 04): Auth gets a token used by every later request; Happy Path
  Lifecycle walks the full search → purchase → confirm → start/end leg → pay → settle flow;
  Alternative Flows (rollback, cancel) each purchase their own fresh offer first so they don't
  disturb the happy-path package; Error Scenarios checks 401/404/409/501/400 - the 409 one
  specifically relies on the happy-path package already being `SETTLED`. Run the **whole
  collection** (Collection Runner, or plain `newman run ...`) for everything to pass; running a
  single folder out of order may hit a request that depends on state an earlier folder would have set up.

## Simulating different providers

In the real TOMP ecosystem every operator (MSP) runs its own TOMP-API; a MaaS platform calls each
one separately. This sandbox mirrors that: each running instance simulates exactly **one**
operator, with its own mode and example vehicles in Amsterdam and/or Utrecht
(`src/data/providers.js`), picked with `SANDBOX_PROVIDER`:

| `SANDBOX_PROVIDER` | Operator | Mode | Cities |
|---|---|---|---|
| `gosharing` (default) | GoSharing | shared bicycle | Amsterdam, Utrecht |
| `felyx` | Felyx | shared moped | Amsterdam, Utrecht |
| `check` | Check | shared bicycle | Amsterdam |
| `uber` | Uber | taxi | Amsterdam, Utrecht |
| `bolt` | Bolt | taxi | Amsterdam |
| `viavan` | ViaVan | taxi | Utrecht |

`search-offers` always returns a walking offer, plus the active provider's own offer **only**
when `travel_specification.from` falls within that provider's seeded coverage - so a taxi-only
provider never returns a BICYCLE offer, and `check`/`bolt` return nothing extra for a pickup near
Utrecht. `GET /health` echoes which operator the instance is running as, which is handy once
several are running side by side. Some real-world example coordinates to search from:

- Amsterdam Centraal: `gps:52.3791,4.9003`
- Amsterdam De Pijp: `gps:52.3550,4.8900`
- Utrecht Centraal: `gps:52.0894,5.1077`
- Utrecht Science Park: `gps:52.0866,5.1704`

Run several operators at once with `start-providers`, which gives each its own port and data file
(`:4010`, `:4011`, ... and `.data/<provider>.json`) so they don't overwrite each other's state:

```powershell
# Windows PowerShell - opens one window per provider
.\start-providers.ps1
.\start-providers.ps1 4                # first 4 providers from the default pool
.\start-providers.ps1 gosharing uber   # or pick your own set
```

```bash
# macOS/Linux/Git Bash - logs to logs/<provider>.log, Ctrl+C stops all of them
./start-providers.sh
./start-providers.sh 4
./start-providers.sh gosharing uber
```

Both default to just `gosharing`. Pass a number (up to 4) to start that many from the default
pool - `gosharing`, `uber`, `check`, `viavan` - a mix of bike-share and taxi, multi-city and
single-city, so the different coverage areas are easy to compare. Or pass explicit provider keys
to pick your own set.

## What's implemented

One full, provable lifecycle: search offers → fetch an offer → purchase it (package `PENDING`)
→ confirm (`CONFIRMED`) → start/end a leg (`STARTED`/`ENDED`, leg `IN_USE`/`ENDED`) → list and
confirm payments (package `SETTLED`) → or cancel/rollback instead.

On top of that, it exposes the generic **OGC API - Features / OGC API - Processes** discovery
surface that `TOMP-API.yaml` itself layers its `package`/`leg` operations on, driven by
`src/data/catalog.js` so it always reflects exactly what this sandbox implements. Every endpoint
below renders a human-browsable HTML page by default; pass `?f=json` for the raw JSON:

| Endpoint | Behavior |
|---|---|
| `GET /` | landing page with links to `/conformance`, `/api`, `/collections`, `/processes` |
| `GET /api` | an interactive Swagger UI for the OpenAPI document (`../TOMP-API.yaml`), "Try it out" included - calls this same running instance; same as `?f=html`. `?f=yaml` returns the raw document, `?f=json` returns it parsed as JSON |
| `GET /conformance` | OGC API - Features/Processes conformance classes this sandbox satisfies |
| `GET /collections` | the collections this sandbox serves: `offers`, `packages`, `payments`, `travel-documents` |
| `GET /collections/{collectionId}` | metadata for one collection; **404** for an unknown id |
| `GET /processes` | summaries of the implemented processes below, each with a `execute` link |
| `GET /processes/{processId}` | description of one process; **501** for a real TOMP-API processId that's out of scope (see below), **404** for anything else |

| Endpoint | Behavior |
|---|---|
| `POST /oauth/token` | issues a real HS256-signed dev Bearer JWT (any non-empty `client_id`/`client_secret` unless `SANDBOX_STRICT_AUTH=true`) |
| `GET /health` | liveness check |
| `POST /processes/search-offers/execution` | generates 2 synthetic offers for the given `travel_specification`, each with a `purchase-offers` or `select-offers` action link (see "Offer links" below) |
| `GET /collections/offers/items?offerId=` | full offer detail (package-shaped) |
| `POST /processes/select-offers/execution` | reserves one or more offers into a **persisted** package (`PENDING`, not yet purchased); the offer(s) are consumed |
| `POST /processes/purchase-package/execution` | purchases a package that was only reserved via `select-offers`; stays `PENDING`, now awaiting `confirm-purchase` |
| `POST /processes/purchase-offers/execution` | creates a **persisted** package (`PENDING`) from an offer; the offer is consumed |
| `POST /processes/extend-expiry-time/execution` | requests more time before a `PENDING` package's rollback window runs out |
| `POST /processes/confirm-purchase/execution` | `PENDING` → `CONFIRMED`; generates the package's payment entry |
| `POST /processes/rollback-purchase/execution` | `PENDING`/`CONFIRMED` → `ROLLBACK` |
| `GET /collections/packages/items?packageId=` | current package + leg state, with status-appropriate action links (see "Package links" below) |
| `POST /processes/start-leg/execution` | leg `NOT_STARTED` → `IN_USE`; package `CONFIRMED` → `STARTED` |
| `POST /processes/pause-leg/execution`, `resume-leg` | leg `IN_USE` ↔ `PAUSED` |
| `POST /processes/end-leg/execution` | leg → `ENDED`; package → `ENDED` once every leg has ended |
| `GET /collections/payments/items` | journal entries for a package (filter by `package`, `invoiceState`, `category`) |
| `POST /processes/confirm-payment/execution` | marks a payment `INVOICED`; package → `SETTLED` once every payment is invoiced |
| `POST /processes/cancel-package/execution` | `CONFIRMED`/`STARTED` → `CANCELLED` |
| `GET /collections/travel-documents/items?packageId=` | travel documents for a `CONFIRMED`+ package - e.g. `unlock-data`/a `boarding-code` link per leg; **409** before `CONFIRMED` |

Invalid transitions (e.g. confirming a package twice) return **HTTP 409** in the spec's own
error envelope: `{ "errors": [{ "errorcode", "type", "title", "status", "detail", "instance" }] }`.

### Offer links

Each offer in a `search-offers` result carries, besides its `self` link, one action link that
reflects how that mode is actually booked in the real world:

- **`purchase-offers`** - self-service modes (walking, shared bicycle/moped) can be bought
  straight away.
- **`select-offers`** - a dispatched ride (taxi) has to be reserved first; this process turns one
  or more offers into a `PENDING` package (just like `purchase-offers` does), which you then still
  run through `confirm-purchase`/`rollback-purchase` as usual.

Which link an offer gets is driven by its mode (`src/lib/store.js`'s `buildOfferVariants`): `TAXI`
offers (`uber`, `bolt`, `viavan`) get `select-offers`; everything else gets `purchase-offers`. Both
links carry a prefilled `body` with the offer id(s) already filled in, per the spec's `link` schema.

### Package links

Every package response (`purchase-offers`, `select-offers`, `purchase-package`,
`confirm-purchase`, ..., and plain `GET /collections/packages/items`) carries, besides its `self`
link, the action links appropriate for its *current* status (`src/lib/geojson.js`'s
`packageActionLinks`):

- **`PENDING`, only reserved** (created by `select-offers`, not yet purchased) - a single
  **`purchase-package`** link to actually purchase it.
- **`PENDING`, purchased** (created directly by `purchase-offers`, or by `purchase-package` on a
  reservation) - **`confirm-purchase`**, **`extend-expiry-time`** and **`rollback-purchase`**: it
  still has to be confirmed (or rolled back, free of charge) before `rollbackExpiresAt`, and that
  window can be extended.
- **`CONFIRMED`** - **`cancel-package`** and **`travel-documents`**: both parties have agreed to
  deliver the service, so the only ways forward are to cancel it or to fetch what's needed to
  actually use it (e.g. the `unlock-data` to open a shared bike/moped, or a `boarding-code` for a
  taxi - see `GET /collections/travel-documents/items?packageId=` above).

These two "flavors" of `PENDING` are otherwise identical (same `status`); only an internal
`purchaseStage` field (`'selected'` vs `'purchased'`, not part of the public schema) tells them
apart, since a reservation and an actual pending purchase both have to show up as `PENDING` per
`TOMP-API.yaml`'s `packageStatus` enum.

### Out of scope (not silently dropped - just not built yet)

`purchase-product`, `use-asset`; `extend-leg`/`postpone-leg` (return `501`); PRE-SALES beyond
`select-offers` and what's implied by search/purchase (`assign-asset`, `assign-ancillary`,
`update-traveller`, `update-travel-specification`, `release-package`, assets/ancillaries
collections); EXECUTE's `{assetOperation}-asset` and `{productOperation}-product`; AFTER-SALES
redress-options and `refund-deposit`; the DISCOVERY, SUPPORT, CUSTOMER and draft modules; the
NOTIFY push-notification module (needs a second actor). These can be added later without
restructuring - see `src/routes/`, one file per module.

## Design notes

- **Persistence**: in-memory `Map`s (`src/lib/store.js`) mirrored to a single JSON file
  (`.data/store.json` by default) on every mutation, and reloaded on startup - so data survives a
  restart without needing a database to install or configure. Set `SANDBOX_PERSIST=false` to run
  purely in-memory (e.g. for a clean-slate demo); the test suite always does this, so test runs
  never touch the real data file. See `.env.example` for `SANDBOX_DATA_FILE`. Start with `--reset`
  (or `npm run start:reset`) to delete the data file before starting, for a clean slate.
- **Auth**: only `BearerAuth` is really implemented (dev JWT via `/oauth/token`). The spec's
  `BasicAuth`/`OAuth`/`OAuthPKI` alternatives are not separately implemented; any operation that
  lists one of them as an alternative to `BearerAuth` still works with a Bearer token in practice.
  OpenAPI-level security enforcement is disabled (`validateSecurity: false`) so our own
  `middleware/auth.js` is the single source of truth - this also sidesteps the spec listing
  security requirements on `/oauth/token` itself (the endpoint used to *obtain* a token).
- **Response validation** is off by default (`VALIDATE_RESPONSES=false`). The spec's own `error`
  schema types `errorcode`/`status` as `tinyInt` (0-10), which real HTTP status codes like 404/409
  exceed - turning response validation on will fail every error response for that reason. Request
  validation is always on.
- **Known upstream spec issues worked around** (both pre-existing, unrelated to any endpoint this
  sandbox implements):
  - `TOMP-API.yaml`'s `verifiableCredential` schema fails strict schema-of-a-schema validation
    (bad `examples` placement, malformed `$ref`) - whole-document validation is disabled
    (`validateApiSpec: false`) so per-request/response validation still runs against everything else.
  - `placeReference`'s `pattern` contains a literal, invalid-regex documentation placeholder
    (`{datasource-prefix}`). `src/lib/loadSpec.js` patches just that one pattern in a cached copy
    of the spec before handing it to the validator (falls through untouched once upstream fixes it).

## Try it end-to-end

```bash
npm start   # :4010

TOKEN=$(curl -s -X POST localhost:4010/oauth/token \
  -d grant_type=client_credentials -d client_id=demo -d client_secret=demo \
  | node -pe "JSON.parse(require('fs').readFileSync(0,'utf8')).access_token")
AUTH=(-H "Authorization: Bearer $TOKEN" -H "Accept-Language: en-US" -H "Content-Type: application/json")

curl -s -X POST localhost:4010/processes/search-offers/execution "${AUTH[@]}" \
  -d '{"inputs":{"type":"searchOffer","specification":{"type":"travel_specification","from":"gps:52.3791,4.9003","to":"gps:52.3550,4.8900"}}}' \
  | tee offers.json | node -pe "JSON.parse(require('fs').readFileSync(0,'utf8')).features.map(f=>f.id)"
# with the default SANDBOX_PROVIDER=gosharing, this Amsterdam pickup returns a walking offer
# *and* a GoSharing shared-bicycle offer - see "Simulating different providers" above
OFFER_ID=$(node -pe "JSON.parse(require('fs').readFileSync('offers.json','utf8')).features[0].id")

curl -s -X POST localhost:4010/processes/purchase-offers/execution "${AUTH[@]}" \
  -d "{\"inputs\":{\"offer\":\"$OFFER_ID\"}}" | tee package.json \
  | node -pe "JSON.parse(require('fs').readFileSync(0,'utf8')).properties.status"   # PENDING
PKG_ID=$(node -pe "JSON.parse(require('fs').readFileSync('package.json','utf8')).properties.id")
LEG_ID=$(node -pe "JSON.parse(require('fs').readFileSync('package.json','utf8')).features[0].id")

curl -s -X POST localhost:4010/processes/confirm-purchase/execution "${AUTH[@]}" \
  -d "{\"inputs\":{\"package\":\"$PKG_ID\"}}" | node -pe "JSON.parse(require('fs').readFileSync(0,'utf8')).properties.status"   # CONFIRMED

curl -s -X POST localhost:4010/processes/start-leg/execution "${AUTH[@]}" \
  -d "{\"inputs\":{\"leg\":\"$LEG_ID\",\"package\":\"$PKG_ID\"}}" | node -pe "JSON.parse(require('fs').readFileSync(0,'utf8')).properties.status"   # STARTED

curl -s -X POST localhost:4010/processes/end-leg/execution "${AUTH[@]}" \
  -d "{\"inputs\":{\"leg\":\"$LEG_ID\",\"package\":\"$PKG_ID\"}}" | node -pe "JSON.parse(require('fs').readFileSync(0,'utf8')).properties.status"   # ENDED

curl -s "localhost:4010/collections/payments/items?package=$PKG_ID" "${AUTH[@]}" | tee payments.json
PAYMENT_ID=$(node -pe "JSON.parse(require('fs').readFileSync('payments.json','utf8')).features[0].id")
curl -s -X POST localhost:4010/processes/confirm-payment/execution "${AUTH[@]}" -d "{\"inputs\":{\"paymentId\":\"$PAYMENT_ID\"}}" -i   # 204

curl -s "localhost:4010/collections/packages/items?packageId=$PKG_ID" "${AUTH[@]}" | node -pe "JSON.parse(require('fs').readFileSync(0,'utf8')).properties.status"   # SETTLED

# negative test: repeating confirm-purchase on a SETTLED package returns 409 + the spec's error envelope
curl -s -i -X POST localhost:4010/processes/confirm-purchase/execution "${AUTH[@]}" -d "{\"inputs\":{\"package\":\"$PKG_ID\"}}"
```
