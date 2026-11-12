const { Router } = require('express');
const fs = require('node:fs');
const yaml = require('js-yaml');

const config = require('../config');
const { TompError } = require('../lib/errors');
const { applyStandardHeaders } = require('../lib/geojson');
const { COLLECTIONS, PROCESSES, OUT_OF_SCOPE_PROCESS_IDS } = require('../data/catalog');

// Generic OGC API - Features / OGC API - Processes discovery surface (landing page, conformance,
// collection and process catalogs) that TOMP-API.yaml layers its own `package`/`leg` operations
// on top of. These describe exactly what this sandbox instance implements, not the full spec -
// see README.md "What's implemented" / "Out of scope".

const router = Router();

function link(rel, href, extra = {}) {
  return { rel, href, ...extra };
}

function describeCollection(collection) {
  return {
    id: collection.id,
    title: collection.title,
    description: collection.description,
    links: [
      link('self', `/collections/${collection.id}`),
      link('items', `/collections/${collection.id}/items`, { type: 'application/geo+json' }),
    ],
  };
}

function processSummary(process) {
  return {
    id: process.id,
    version: '1.0.0',
    title: process.title,
    description: process.description,
    jobControlOptions: ['sync-execute'],
    links: [
      link('self', `/processes/${process.id}`),
      link('execute', `/processes/${process.id}/execution`, { method: 'POST' }),
    ],
  };
}

// All the discovery/metadata endpoints below (landing page, conformance, collections, processes)
// follow the same OGC API convention: ?f=json returns the raw JSON, anything else (including no
// `f` at all) renders a human-browsable HTML page - same default-to-html as GET /api.
const NAV_LINKS = [
  ['/', 'landing page'],
  ['/conformance', 'conformance'],
  ['/collections', 'collections'],
  ['/processes', 'processes'],
  ['/api', 'API doc'],
];

function renderHtmlPage(title, data) {
  const nav = NAV_LINKS.map(([href, label]) => `<a href="${href}">${label}</a>`).join('\n    ');
  const links = Array.isArray(data.links) ? data.links : [];
  const linksHtml = links
    .map((l) => `<li><a href="${l.href}">${l.rel}</a>${l.type ? ` <span class="type">(${l.type})</span>` : ''}</li>`)
    .join('\n      ');
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>${title} - TOMP-API Sandbox</title>
  <style>
    body { font-family: system-ui, sans-serif; max-width: 860px; margin: 2rem auto; padding: 0 1rem; color: #1a1a1a; }
    nav { margin-bottom: 1.5rem; }
    nav a { margin-right: 1rem; }
    pre { background: #f6f8fa; padding: 1rem; overflow-x: auto; border-radius: 6px; }
    ul { padding-left: 1.2rem; }
    .type { color: #666; font-size: 0.85em; }
    a { color: #0969da; }
  </style>
</head>
<body>
  <nav>
    ${nav}
  </nav>
  <h1>${title}</h1>
  ${linksHtml ? `<ul>\n      ${linksHtml}\n    </ul>` : ''}
  <pre>${JSON.stringify(data, null, 2)}</pre>
</body>
</html>`;
}

function sendNegotiated(req, res, status, title, data) {
  if (req.query.f === 'json') {
    return res.status(status).json(data);
  }
  return res.status(status).type('html').send(renderHtmlPage(title, data));
}

router.get('/', (req, res) => {
  sendNegotiated(req, res, 200, 'Landing page', {
    title: 'TOMP-API Sandbox',
    description:
      'A stateful sandbox implementing a subset of the TOMP-API v2 lifecycle, built on the ' +
      'OGC API - Features/Processes patterns TOMP-API.yaml itself uses. GET /conformance, ' +
      '/collections and /processes describe exactly what this running instance supports.',
    links: [
      link('self', '/'),
      link('conformance', '/conformance'),
      link('service-desc', '/api?f=yaml', { type: 'application/yaml' }),
      link('service-doc', '/api?f=html', { type: 'text/html' }),
      link('data', '/collections'),
      link('http://www.opengis.net/def/rel/ogc/1.0/processes', '/processes'),
    ],
  });
});

function renderSwaggerUiHtml() {
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>TOMP-API Sandbox - API docs</title>
  <link rel="stylesheet" href="/api-assets/swagger-ui.css">
  <style>body { margin: 0; }</style>
</head>
<body>
  <div id="swagger-ui"></div>
  <script src="/api-assets/swagger-ui-bundle.js"></script>
  <script>
    // The spec lists BasicAuth/BearerAuth/OAuth/OAuthPKI/OpenData as alternatives on most
    // operations, but this sandbox's own middleware (middleware/auth.js) only ever checks for a
    // raw Bearer header - none of those other schemes are separately implemented, and showing them
    // in the Authorize dialog just invites clicking the wrong one (OAuth's authorizationCode flow
    // opens a popup at authorizationUrl: "/", which is just this sandbox's landing page - there's
    // no login screen behind it to redirect back from). So for this rendered copy of the spec only,
    // every security requirement is replaced with a single dedicated oauth2 clientCredentials
    // scheme, and every other scheme is dropped from components.securitySchemes - the Authorize
    // dialog then has exactly one thing to fill in.
    const SANDBOX_TOKEN_SCHEME = 'SandboxDevToken';
    const SANDBOX_TOKEN_REQUIREMENT = [{ [SANDBOX_TOKEN_SCHEME]: ['processes'] }];

    function replaceWithSandboxTokenOnly(security) {
      // An explicit empty security array means "no auth for this operation" (an override of the
      // global default) - leave that alone rather than newly demanding a token for it.
      if (!Array.isArray(security) || security.length === 0) return security;
      return SANDBOX_TOKEN_REQUIREMENT;
    }

    const HTTP_METHODS = ['get', 'put', 'post', 'delete', 'options', 'head', 'patch', 'trace'];

    function enableSandboxTokenOnly(spec) {
      spec.components = spec.components || {};
      spec.components.securitySchemes = {
        [SANDBOX_TOKEN_SCHEME]: {
          type: 'oauth2',
          description:
            'Sandbox-only shortcut (not part of the real TOMP-API spec): fill in any non-empty ' +
            'client id/secret and hit Authorize here - Swagger UI will call POST /oauth/token for ' +
            'you and use the resulting access_token as the Bearer header from then on.',
          flows: {
            clientCredentials: {
              tokenUrl: '/oauth/token',
              scopes: { processes: 'Access to /processes/' },
            },
          },
        },
      };
      if (spec.security) spec.security = replaceWithSandboxTokenOnly(spec.security);
      Object.values(spec.paths || {}).forEach((pathItem) => {
        HTTP_METHODS.forEach((method) => {
          const operation = pathItem[method];
          if (operation && operation.security) {
            operation.security = replaceWithSandboxTokenOnly(operation.security);
          }
        });
      });
      return spec;
    }

    // Every operation's Accept-Language header parameter is the same shared
    // components.parameters.acceptLanguage object (34 $ref's resolved by swagger-client against
    // this one fetched spec), so setting its example here pre-fills "Try it out" for all of them
    // in one place, instead of leaving every tester to type it in by hand. (schema.default isn't
    // used here: schema is itself a $ref to components/schemas/shortString, and OAS3 dereferencing
    // drops sibling keys next to a $ref, so a default stuffed in there wouldn't survive resolution.)
    function defaultAcceptLanguageToEnglish(spec) {
      const param = spec.components && spec.components.parameters && spec.components.parameters.acceptLanguage;
      if (!param) return spec;
      param.example = 'en-GB';
      return spec;
    }

    window.onload = async () => {
      const spec = enableSandboxTokenOnly(await (await fetch('/api?f=json')).json());
      defaultAcceptLanguageToEnglish(spec);
      // TOMP-API.yaml's own servers: is a placeholder (https://example.to.eu/tomp/v2) - override
      // it with wherever this instance actually runs, so "Try it out" hits it instead of that URL.
      spec.servers = [{ url: window.location.origin }];
      window.ui = SwaggerUIBundle({
        spec,
        dom_id: '#swagger-ui',
        presets: [SwaggerUIBundle.presets.apis],
        // "Try it out" calls this same sandbox instance directly (same origin, CORS already
        // enabled in app.js) - handy for poking at a running instance, but it's a real request
        // against its stateful store, not a dry run.
        deepLinking: true,
      });
      // Pre-fills the SandboxDevToken Authorize section with the sandbox's non-strict dev
      // credentials (any non-empty client_id/client_secret is accepted unless
      // SANDBOX_STRICT_AUTH=true) - still requires clicking "Authorize" yourself, which is what
      // actually calls /oauth/token.
      window.ui.initOAuth({ clientId: 'demo', clientSecret: 'demo', scopes: 'processes' });
    };
  </script>
</body>
</html>`;
}

router.get('/api', (req, res) => {
  // no-store: without it, a browser that cached an earlier response (from before a Content-Type
  // change, or from visiting a different ?f= variant) revalidates via ETag, gets 304, and keeps
  // reusing that stale cached response's headers - e.g. still prompting a download.
  res.set('Cache-Control', 'no-store');
  const raw = fs.readFileSync(config.specPath, 'utf8');
  if (req.query.f === 'json') {
    return res.status(200).json(yaml.load(raw));
  }
  if (req.query.f === 'yaml') {
    // text/plain, not text/yaml or application/yaml: browsers only render a handful of hardcoded
    // MIME types inline (text/plain among them) and "Save As" prompt everything else, yaml included.
    return res.status(200).type('text/plain; charset=utf-8').send(raw);
  }
  // Default (and explicit f=html): an interactive Swagger UI, not the raw document - friendlier
  // for the common case of a human opening /api in a browser. Machine/CLI clients want
  // ?f=yaml/json.
  return res.status(200).type('html').send(renderSwaggerUiHtml());
});

router.get('/conformance', (req, res) => {
  sendNegotiated(req, res, 200, 'Conformance', {
    conformsTo: [
      'http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/core',
      'http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/geojson',
      'http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/oas30',
      'http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/core',
      'http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/json',
      'http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/oas30',
      'https://github.com/TOMP-WG/TOMP-API',
    ],
  });
});

router.get('/collections', (req, res) => {
  applyStandardHeaders(res);
  sendNegotiated(req, res, 200, 'Collections', {
    links: [link('self', '/collections')],
    collections: COLLECTIONS.map(describeCollection),
  });
});

router.get('/collections/:collectionId', (req, res, next) => {
  const found = COLLECTIONS.find((c) => c.id === req.params.collectionId);
  if (!found) {
    return next(
      new TompError({
        errorcode: 2,
        type: 'NOTFOUND',
        status: 404,
        instance: req.originalUrl,
        title: 'Unknown collection',
        detail: `No collection named '${req.params.collectionId}'`,
      }),
    );
  }
  applyStandardHeaders(res);
  return sendNegotiated(req, res, 200, `Collection: ${found.id}`, describeCollection(found));
});

router.get('/processes', (req, res) => {
  sendNegotiated(req, res, 200, 'Processes', {
    links: [link('self', '/processes')],
    processes: PROCESSES.map(processSummary),
  });
});

router.get('/processes/:processId', (req, res, next) => {
  const { processId } = req.params;
  const implemented = PROCESSES.find((p) => p.id === processId);
  if (implemented) {
    return sendNegotiated(req, res, 200, `Process: ${processId}`, {
      ...processSummary(implemented),
      inputs: implemented.inputs,
      outputs: implemented.outputs,
    });
  }
  if (OUT_OF_SCOPE_PROCESS_IDS.has(processId)) {
    return next(
      new TompError({
        errorcode: 9,
        type: 'SCOPE',
        status: 501,
        instance: req.originalUrl,
        title: 'Process not implemented',
        detail: `${processId} is a valid TOMP-API process but out of scope for this sandbox - see README.md`,
      }),
    );
  }
  return next(
    new TompError({
      errorcode: 2,
      type: 'NOTFOUND',
      status: 404,
      instance: req.originalUrl,
      title: 'Unknown process',
      detail: `No process named '${processId}'`,
    }),
  );
});

module.exports = router;
