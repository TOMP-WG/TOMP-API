# TOMP-VC for dummies

A plain-language guide to the `verifiableCredential` schema (`TOMP-API-1-CORE.yaml`), which lets a
traveller attach digital, cryptographically verifiable proof of a claim - e.g. "I hold a category B
driver license" - to a `searchOfferRequest` (`TOMP-API-2-OFFERS.yaml`). It sits inside
`traveller.characteristics.verifiableCredentials`, so it's always scoped to one specific traveller
in the request.

This guide does not replace the schema - it explains the *why* behind it, with three worked examples.

## 1. The problem it solves

Some offers depend on something only the traveller can prove: "I'm old enough", "I have a valid
driver license", "I'm entitled to a disability discount". Today that's usually checked by eyeballing
a physical card. A **Verifiable Credential (VC)** is the digital equivalent: a claim, digitally
signed by whoever is authoritative for it (e.g. the RDW for a Dutch driver license), that a computer
can check instead of a human.

## 2. Two signatures, two different questions

This is the part that trips most people up, so it gets its own section.

| | Signed by | Proves | Claim |
|---|---|---|---|
| **VC** (Verifiable Credential) | the **issuer** (e.g. RDW) | "this claim is genuine and unaltered" | *"RDW states: this license (category B) exists"* |
| **VP** (Verifiable Presentation) | the **holder** (the traveller's wallet) | "whoever is presenting this, right now, actually controls it" | *"I am the one submitting this VC, right now, to you"* |

A bare VC is just a signed blob of text - and text can be copied. Without a holder signature, anyone
who got hold of a copy (a screenshot, a leaked log line) could resubmit it and pass as the original
owner. A **VP wraps a VC and adds the holder's own signature**, over a one-time **challenge** issued
by whoever is asking for it, so a replayed/stolen copy is detected and rejected.

Rule of thumb: a bare VC is enough to trust the *claim*; you need a VP to also trust *who's
presenting it, right now*.

## 3. Who talks to the wallet? (the architecture)

The traveller's proof lives in **their own wallet app**, on their own phone. Two parties could
theoretically ask that wallet for a presentation - but only one of them has a practical way to reach
it:

```
 traveller's wallet app (on their phone)
        ▲
        │ deep link (same device) or QR code (cross-device)
        │ "please prove X, here's my nonce + client_id"
        │
        │ signed VP back
        ▼
 ┌─────────────┐        offer/booking request         ┌─────────────┐
 │     MP      │ ────────────────────────────────────▶│     TO      │
 │ (has the    │   (VP embedded as opaque evidence     │ (no app on  │
 │  traveller's│    in traveller.characteristics)      │  the        │
 │  app/session)                                       │  traveller's│
 └─────────────┘                                       │  device)    │
                                                        └─────────────┘
```

- The **MP** owns the app/session the traveller is actually using, so the MP is the one that runs the
  presentation exchange directly with the wallet (this is the **OpenID4VP** protocol, in a nutshell:
  a deep link or QR code carrying a `client_id` and `nonce`, answered by a signed VP).
- The **TO** has no such channel - it never talks to the wallet. It receives the MP's already-collected
  VP as an opaque string inside the offer request, and **trusts that relay**: it can still
  cryptographically verify the VP/VC signatures itself, but it cannot independently re-challenge the
  wallet to confirm the binding to "this" traveller.

This is why `domain` (who the challenge was for) and `challenge` (the nonce itself) in the schema will,
in practice, usually identify the **MP** - not the TO.

## 4. Attribute reference

| Attribute | Required | Meaning |
|---|---|---|
| `type` | yes | `VERIFIABLE_CREDENTIAL` (issuer-signed, bare claim) or `VERIFIABLE_PRESENTATION` (holder-signed wrapper, adds proof of possession). |
| `format` | yes | Serialization: `JWT_VC`/`JWT_VP` (compact JWT), `LDP_VC`/`LDP_VP` (JSON-LD + Linked Data Proof), `SD_JWT` (selective disclosure, used by the EU Digital Identity Wallet), `MDOC` (ISO/IEC 18013-5 CBOR, used by mobile driving licences). |
| `proves` | no | What claim this is evidence for: `LICENSE`, `AGE`, `IDENTITY`, `ENTITLEMENT`, `CARD`, `OTHER`. The actual details (e.g. the license category) live *inside* `credential`, not here - so they can't be spoofed independently of the signature. |
| `subject` | no | The holder identifier (DID, or for an mdoc the document number), repeated in plaintext purely so an MP/TO can quickly route this to the right traveller. **Not proof by itself** - always re-derived from, and checked against, the signed `credential`. |
| `domain` | no, only for VPs | Who the presentation was signed for (the `aud` of a JWT-VP) - in practice the **MP**'s client ID/app URI, per the architecture above. |
| `challenge` | no, only for VPs | The one-time nonce the verifier issued and the holder's wallet signed over (the `nonce` of a JWT-VP) - prevents replay of a captured VP. How it's exchanged (deep link/QR) is out of scope for this schema. |
| `credential` | yes | The actual encoded evidence: a JWT string, a JSON-LD document, or (for `MDOC`) a base64url-encoded CBOR structure. This is the only field whose content is cryptographically trustworthy - everything else here is a plaintext convenience copy of what's (or should be) inside it. |
| `issuer` | no | Identifier of whoever vouches for the claim (e.g. `did:web:rdw.nl`), when not already embedded in `credential`. |
| `customFields` | no | Free-form bilateral extension point, like elsewhere in TOMP-API. |

## 5. Three worked examples

### 5.1 A bare VC - "RDW says: this is a valid category B license"

The simplest case: just the issuer's signed claim, no holder-binding.

```json
{
  "type": "VERIFIABLE_CREDENTIAL",
  "format": "JWT_VC",
  "proves": "LICENSE",
  "subject": "did:key:z6MkhaXgBZDvotDkL5257faiztiGiC2QtKLGpbnnXv1Ch1zy",
  "credential": "eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImRpZDp3ZWI6cmR3Lm5sI2tleS0xIn0.eyJpc3MiOiJkaWQ6d2ViOnJkdy5ubCIsInN1YiI6ImRpZDprZXk6ejZNa2hhWGdCWkR2b3REa0w1MjU3ZmFpenRpR2lDMlF0S0xHcGJublh2MUNoMXp5IiwibmJmIjoxNzAwMDAwMDAwLCJ2YyI6eyJAY29udGV4dCI6WyJodHRwczovL3d3dy53My5vcmcvMjAxOC9jcmVkZW50aWFscy92MSJdLCJ0eXBlIjpbIlZlcmlmaWFibGVDcmVkZW50aWFsIiwiRHJpdmVyTGljZW5zZUNyZWRlbnRpYWwiXSwiY3JlZGVudGlhbFN1YmplY3QiOnsiaWQiOiJkaWQ6a2V5Ono2TWtoYVhnQlpEdm90RGtMNTI1N2ZhaXp0aUdpQzJRdEtMR3Bibm5YdjFDaDF6eSIsImxpY2Vuc2VDYXRlZ29yeSI6IkIiLCJsaWNlbnNlTnVtYmVyIjoiTkwtMTIzNDU2NyIsImlzc3VpbmdDb3VudHJ5IjoiTkwifX19.hqm-Gv0e1sJ4yBnxvkJfRzWHqWdpKUhzJ4fGm0X3n8w",
  "issuer": "did:web:rdw.nl"
}
```

If you paste the `credential` JWT into a decoder (e.g. jwt.io - header/payload only, the fake
signature here won't verify), you'd see the payload underneath:

```json
{
  "iss": "did:web:rdw.nl",
  "sub": "did:key:z6MkhaXgBZDvotDkL5257faiztiGiC2QtKLGpbnnXv1Ch1zy",
  "nbf": 1700000000,
  "vc": {
    "@context": ["https://www.w3.org/2018/credentials/v1"],
    "type": ["VerifiableCredential", "DriverLicenseCredential"],
    "credentialSubject": {
      "id": "did:key:z6MkhaXgBZDvotDkL5257faiztiGiC2QtKLGpbnnXv1Ch1zy",
      "licenseCategory": "B",
      "licenseNumber": "NL-1234567",
      "issuingCountry": "NL"
    }
  }
}
```

`iss` is RDW, `sub`/`credentialSubject.id` is the (pseudonymous) holder, and `credentialSubject`
carries the actual license details. jwt.io will complain it can't fetch a public key for `did:web:rdw.nl`
(it only knows how to fetch JWKS from a plain HTTPS URL) - that's expected, a real verifier resolves
DIDs with a DID-aware library, not a generic JWT tool.

### 5.2 The same VC, as actually collected - wrapped in a VP

This is what the MP would realistically submit: the VC above, plus a holder signature over an
MP-issued challenge, proving the current submitter really controls `did:key:z6Mk...`.

```json
{
  "type": "VERIFIABLE_PRESENTATION",
  "format": "JWT_VP",
  "proves": "LICENSE",
  "subject": "did:key:z6MkhaXgBZDvotDkL5257faiztiGiC2QtKLGpbnnXv1Ch1zy",
  "domain": "https://app.example-mp.nl",
  "challenge": "4f9c2e71-8b3a-4c2d-9e4a-7a5b6c1d2e3f",
  "credential": "eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCIsImtpZCI6ImRpZDprZXk6ejZNa2hhWGdCWkR2b3REa0w1MjU3ZmFpenRpR2lDMlF0S0xHcGJublh2MUNoMXp5I3o2TWtoYVhnQlpEdm90RGtMNTI1N2ZhaXp0aUdpQzJRdEtMR3Bibm5YdjFDaDF6eSJ9.eyJpc3MiOiJkaWQ6a2V5Ono2TWtoYVhnQlpEdm90RGtMNTI1N2ZhaXp0aUdpQzJRdEtMR3Bibm5YdjFDaDF6eSIsInN1YiI6ImRpZDprZXk6ejZNa2hhWGdCWkR2b3REa0w1MjU3ZmFpenRpR2lDMlF0S0xHcGJublh2MUNoMXp5IiwiYXVkIjoiaHR0cHM6Ly9hcHAuZXhhbXBsZS1tcC5ubCIsIm5vbmNlIjoiNGY5YzJlNzEtOGIzYS00YzJkLTllNGEtN2E1YjZjMWQyZTNmIiwibmJmIjoxNzAwMDAwMTAwLCJ2cCI6eyJAY29udGV4dCI6WyJodHRwczovL3d3dy53My5vcmcvMjAxOC9jcmVkZW50aWFscy92MSJdLCJ0eXBlIjpbIlZlcmlmaWFibGVQcmVzZW50YXRpb24iXSwidmVyaWZpYWJsZUNyZWRlbnRpYWwiOlsiZXlKaGJHY2lPaUpGVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0lzSW10cFpDSTZJbVJwWkRwM1pXSTZjbVIzTG01c0kydGxlUzB4SW4wLmV5SnBjM01pT2lKa2FXUTZkMlZpT25Ka2R5NXViQ0lzSW5OMVlpSTZJbVJwWkRwclpYazZlalpOYTJoaFdHZENXa1IyYjNSRWEwdzFNalUzWm1GcGVuUnBSMmxETWxGMFMweEhjR0p1YmxoMk1VTm9NWHA1SWl3aWJtSm1Jam94TnpBd01EQXdNREF3TENKMll5STZleUpBWTI5dWRHVjRkQ0k2V3lKb2RIUndjem92TDNkM2R5NTNNeTV2Y21jdk1qQXhPQzlqY21Wa1pXNTBhV0ZzY3k5Mk1TSmRMQ0owZVhCbElqcGJJbFpsY21sbWFXRmliR1ZEY21Wa1pXNTBhV0ZzSWl3aVJISnBkbVZ5VEdsalpXNXpaVU55WldSbGJuUnBZV3dpWFN3aVkzSmxaR1Z1ZEdsaGJGTjFZbXBsWTNRaU9uc2lhV1FpT2lKa2FXUTZhMlY1T25vMlRXdG9ZVmhuUWxwRWRtOTBSR3RNTlRJMU4yWmhhWHAwYVVkcFF6SlJkRXRNUjNCaWJtNVlkakZEYURGNmVTSXNJbXhwWTJWdWMyVkRZWFJsWjI5eWVTSTZJa0lpTENKc2FXTmxibk5sVG5WdFltVnlJam9pVGt3dE1USXpORFUyTnlJc0ltbHpjM1ZwYm1kRGIzVnVkSEo1SWpvaVRrd2lmWDE5LmhxbS1HdjBlMXNKNHlCbnh2a0pmUnpXSHFXZHBLVWh6SjRmR20wWDNuOHciXX19.ZFz1y2Kz3nX9sV2hQ4pR8tW6oM1aB7cE0dG5jK3lN9q",
  "issuer": "did:web:rdw.nl"
}
```

Decoded, the holder-signed payload looks like this - note it wraps the *entire previous JWT* as a
string inside `vp.verifiableCredential`:

```json
{
  "iss": "did:key:z6MkhaXgBZDvotDkL5257faiztiGiC2QtKLGpbnnXv1Ch1zy",
  "sub": "did:key:z6MkhaXgBZDvotDkL5257faiztiGiC2QtKLGpbnnXv1Ch1zy",
  "aud": "https://app.example-mp.nl",
  "nonce": "4f9c2e71-8b3a-4c2d-9e4a-7a5b6c1d2e3f",
  "nbf": 1700000100,
  "vp": {
    "@context": ["https://www.w3.org/2018/credentials/v1"],
    "type": ["VerifiablePresentation"],
    "verifiableCredential": ["<the JWT-VC from example 5.1>"]
  }
}
```

`aud`/`nonce` match the schema's `domain`/`challenge` exactly - that's the MP proving to itself (and,
by relaying this onward, implicitly to the TO) that this presentation was made *for this specific
request*, by someone who controls the holder key, not replayed from somewhere else.

### 5.3 A different country, a different format - Danish mdoc

Not every country uses W3C VCs. Denmark's existing "kørekort-app" (and the ISO 18013-5 mobile driving
licence standard it's built on, also used by the upcoming EU Digital Identity Wallet) encodes
everything as signed, binary **CBOR**, not JSON/JWT.

```json
{
  "type": "VERIFIABLE_CREDENTIAL",
  "format": "MDOC",
  "proves": "LICENSE",
  "subject": "DK-9876543",
  "credential": "omdkb2NUeXBldW9yZy5pc28uMTgwMTMuNS4xLm1ETGxpc3N1ZXJTaWduZWSiam5hbWVTcGFjZXOhcW9yZy5pc28uMTgwMTMuNS4xh6JxZWxlbWVudElkZW50aWZpZXJrZmFtaWx5X25hbWVsZWxlbWVudFZhbHVlaEFuZGVyc2VuonFlbGVtZW50SWRlbnRpZmllcmpnaXZlbl9uYW1lbGVsZW1lbnRWYWx1ZWRBbm5honFlbGVtZW50SWRlbnRpZmllcmpiaXJ0aF9kYXRlbGVsZW1lbnRWYWx1ZWoxOTkwLTA1LTEyonFlbGVtZW50SWRlbnRpZmllcm9pc3N1aW5nX2NvdW50cnlsZWxlbWVudFZhbHVlYkRLonFlbGVtZW50SWRlbnRpZmllcnFpc3N1aW5nX2F1dGhvcml0eWxlbGVtZW50VmFsdWVyRsOmcmRzZWxzc3R5cmVsc2VuonFlbGVtZW50SWRlbnRpZmllcm9kb2N1bWVudF9udW1iZXJsZWxlbWVudFZhbHVlakRLLTk4NzY1NDOicWVsZW1lbnRJZGVudGlmaWVycmRyaXZpbmdfcHJpdmlsZWdlc2xlbGVtZW50VmFsdWWBo3V2ZWhpY2xlX2NhdGVnb3J5X2NvZGVhQmppc3N1ZV9kYXRlajIwMTItMDYtMDFrZXhwaXJ5X2RhdGVqMjAzMi0wNi0wMWppc3N1ZXJBdXRoeC9DT1NFX1NpZ24xKC4uLnNpZ25hdHVyZSBvbWl0dGVkIGZvciBicmV2aXR5Li4uKQ",
  "issuer": "Færdselsstyrelsen (DK)"
}
```

Decoded (base64url → CBOR → JSON-ish view):

```json
{
  "docType": "org.iso.18013.5.1.mDL",
  "issuerSigned": {
    "nameSpaces": {
      "org.iso.18013.5.1": [
        { "elementIdentifier": "family_name", "elementValue": "Andersen" },
        { "elementIdentifier": "given_name", "elementValue": "Anna" },
        { "elementIdentifier": "birth_date", "elementValue": "1990-05-12" },
        { "elementIdentifier": "issuing_country", "elementValue": "DK" },
        { "elementIdentifier": "issuing_authority", "elementValue": "Færdselsstyrelsen" },
        { "elementIdentifier": "document_number", "elementValue": "DK-9876543" },
        { "elementIdentifier": "driving_privileges", "elementValue": [
          { "vehicle_category_code": "B", "issue_date": "2012-06-01", "expiry_date": "2032-06-01" }
        ]}
      ]
    },
    "issuerAuth": "COSE_Sign1(...signature omitted for brevity...)"
  }
}
```

Same idea as the JWT-VC (an issuer-signed set of claims), different technical dress: `issuerAuth` here
plays the role `vc`'s JWT signature plays above, and `nameSpaces` the role of `credentialSubject`.
Note this example also shows name and birth date in plaintext - unlike the pseudonymous `did:key` in
the Dutch examples, mdocs are typically issued with identity attributes directly inside, since mobile
driving licences are expected to double as an ID document at a roadside check.

## 6. Putting it in context: a full offer request

```json
{
  "type": "searchOffer",
  "specification": {
    "type": "travelSpecification",
    "from": "place-1",
    "to": "place-2"
  },
  "travellers": [
    {
      "type": "traveller",
      "id": "traveller-1",
      "characteristics": {
        "verifiableCredentials": [
          { "...": "one of the three examples above" }
        ]
      }
    }
  ]
}
```

Because the VC/VP sits inside this specific `traveller` object, the TO already knows *which* traveller
it belongs to from the message structure alone - it doesn't need the credential's own `subject` for
that. What it still can't do, without its own channel to the wallet, is independently confirm that
binding was done correctly - that's the trust it places in the MP (see section 3).

## 7. FAQ

**Q: Can I see the license category/holder just by looking at the schema?**
No - by design. `proves` only tells you *what kind* of claim this is; the actual value lives inside
the signed `credential`, because a plaintext field next to it could be set to anything regardless of
what was actually signed.

**Q: jwt.io says it can't fetch a public key for `did:web:rdw.nl` - is that a bug?**
No. jwt.io only resolves plain HTTPS JWKS URLs. A `did:web` is resolved differently (fetch
`https://rdw.nl/.well-known/did.json`), which only a DID-aware verifier library knows how to do. This
is expected; the examples in this guide are for inspecting *structure*, not for verifying against a
real key (the signatures are placeholders).

**Q: Does `subject: did:key:...` tell me who the person really is?**
No - a DID is a pseudonymous, cryptographic identifier, not a name. Unless the issuer added identity
attributes as separate claims (as the Danish mdoc example does), you only learn "this credential
belongs to whoever controls this key", not a real-world identity.

**Q: Who should run the OpenID4VP challenge - TO or MP?**
The MP. It's the party with an app/session on the traveller's device. The TO receives an
already-verified VP as opaque evidence and trusts that relay.
