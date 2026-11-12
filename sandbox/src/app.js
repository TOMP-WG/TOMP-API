const express = require('express');
const cors = require('cors');
const morgan = require('morgan');
const OpenApiValidator = require('express-openapi-validator');
const swaggerUiAssetPath = require('swagger-ui-dist').absolutePath();

const config = require('./config');
const errorHandler = require('./middleware/errorHandler');
const { TompError } = require('./lib/errors');
const { resolveValidatableSpecPath } = require('./lib/loadSpec');
const store = require('./lib/store');

const healthRoutes = require('./routes/health');
const discoveryRoutes = require('./routes/discovery');
const authRoutes = require('./routes/auth');
const offersRoutes = require('./routes/offers');
const packagesRoutes = require('./routes/packages');
const preSalesRoutes = require('./routes/preSales');
const purchaseRoutes = require('./routes/purchase');
const executionRoutes = require('./routes/execution');
const paymentsRoutes = require('./routes/payments');
const afterSalesRoutes = require('./routes/afterSales');

async function createApp() {
  store.loadFromDisk();

  const app = express();
  app.disable('x-powered-by');
  app.use(cors());
  app.use(morgan('dev'));
  app.use(express.json());
  app.use(express.urlencoded({ extended: false }));

  // Static Swagger UI assets backing GET /api?f=html - kept off the validated API surface
  // entirely (ignoreUndocumented below would let it through anyway, but mounting it first
  // keeps that dependency implicit rather than load-bearing).
  app.use('/api-assets', express.static(swaggerUiAssetPath));

  // The spec lists BasicAuth/BearerAuth/OAuth/OAuthPKI as alternatives on most operations
  // (including, circularly, on /oauth/token itself). This sandbox only implements BearerAuth,
  // enforced per-route by middleware/auth.js, so OpenAPI-level security enforcement is disabled here.
  app.use(
    OpenApiValidator.middleware({
      apiSpec: resolveValidatableSpecPath(),
      validateRequests: { coerceTypes: true },
      validateResponses: config.validateResponses,
      validateSecurity: false,
      ignoreUndocumented: true,
      // TOMP-API.yaml's own `verifiableCredential` schema currently fails strict JSON-Schema-of-a-
      // schema validation (bad `examples` placement, malformed $ref) - a pre-existing spec issue
      // unrelated to any endpoint this sandbox implements. Skip the whole-document check so the
      // validator can still validate individual requests/responses against the rest of the spec.
      validateApiSpec: false,
    }),
  );

  app.use(healthRoutes);
  app.use(discoveryRoutes);
  app.use(authRoutes);
  app.use(offersRoutes);
  app.use(packagesRoutes);
  app.use(preSalesRoutes);
  app.use(purchaseRoutes);
  app.use(executionRoutes);
  app.use(paymentsRoutes);
  app.use(afterSalesRoutes);

  app.use((req, res, next) => {
    next(
      new TompError({
        errorcode: 2,
        type: 'NOTFOUND',
        status: 404,
        title: 'Not found',
        detail: `No route for ${req.method} ${req.originalUrl}`,
      }),
    );
  });

  app.use(errorHandler);
  return app;
}

module.exports = createApp;
