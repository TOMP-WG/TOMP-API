const { Router } = require('express');
const { issueToken } = require('../lib/jwt');
const { TompError } = require('../lib/errors');
const config = require('../config');

const router = Router();

// RFC 6749 #2.3.1: a client may authenticate via HTTP Basic auth instead of client_id/
// client_secret body fields - and Swagger UI's clientCredentials flow always does it this way
// (never puts them in the body), so this is required for "Authorize" in /api to work, not just
// spec compliance.
function clientCredentialsFromBasicAuth(header) {
  if (!header || !header.startsWith('Basic ')) return {};
  const decoded = Buffer.from(header.slice('Basic '.length), 'base64').toString('utf8');
  const separatorIndex = decoded.indexOf(':');
  if (separatorIndex === -1) return {};
  return { clientId: decoded.slice(0, separatorIndex), clientSecret: decoded.slice(separatorIndex + 1) };
}

router.post('/oauth/token', (req, res, next) => {
  const body = req.body || {};
  const basicAuth = clientCredentialsFromBasicAuth(req.headers.authorization);
  const grantType = body.grant_type;
  const clientId = body.client_id || basicAuth.clientId;
  const clientSecret = body.client_secret || basicAuth.clientSecret;

  if (!['client_credentials', 'password'].includes(grantType)) {
    return next(
      new TompError({
        errorcode: 4,
        type: 'AUTH',
        status: 400,
        title: 'Unsupported grant_type',
        detail: 'Sandbox only supports client_credentials (and password as an alias)',
      }),
    );
  }
  if (!clientId || !clientSecret) {
    return next(new TompError({ errorcode: 4, type: 'AUTH', status: 400, title: 'Missing client credentials' }));
  }
  if (config.strictAuth && (clientId !== config.clientId || clientSecret !== config.clientSecret)) {
    return next(new TompError({ errorcode: 4, type: 'AUTH', status: 401, title: 'Invalid client credentials' }));
  }

  const { accessToken, expiresIn } = issueToken(clientId);
  res.status(200).json({ access_token: accessToken, token_type: 'Bearer', expires_in: expiresIn });
  return undefined;
});

module.exports = router;
