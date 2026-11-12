const { TompError } = require('../lib/errors');

// eslint-disable-next-line no-unused-vars
module.exports = function errorHandler(err, req, res, next) {
  if (res.headersSent) {
    return undefined;
  }

  if (err instanceof TompError) {
    return res.status(err.status).json(err.toBody());
  }

  // express-openapi-validator request-validation errors
  if (err.status && Array.isArray(err.errors)) {
    return res.status(err.status).json({
      errors: err.errors.slice(0, 10).map((e, i) => ({
        errorcode: Math.min(9, i + 1),
        type: 'VALID',
        title: String(e.message || 'Request validation failed').slice(0, 75),
        status: err.status,
        detail: `${e.path || ''} ${e.message || ''}`.trim(),
        instance: req.originalUrl,
      })),
    });
  }

  console.error(err);
  return res.status(500).json({
    errors: [
      {
        errorcode: 9,
        type: 'INTERNAL',
        title: 'Internal sandbox error',
        status: 500,
        detail: err.message,
        instance: req.originalUrl,
      },
    ],
  });
};
