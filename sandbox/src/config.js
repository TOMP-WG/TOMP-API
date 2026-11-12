const path = require('node:path');

require('dotenv').config({ path: path.resolve(__dirname, '../.env') });

module.exports = {
  port: parseInt(process.env.PORT, 10) || 4010,
  jwtSecret: process.env.SANDBOX_JWT_SECRET || 'dev-insecure-secret-change-me',
  tokenTtlSeconds: 3600,
  validateResponses: process.env.VALIDATE_RESPONSES === 'true',
  strictAuth: process.env.SANDBOX_STRICT_AUTH === 'true',
  clientId: process.env.SANDBOX_CLIENT_ID || '',
  clientSecret: process.env.SANDBOX_CLIENT_SECRET || '',
  specPath: path.resolve(__dirname, '../../TOMP-API.yaml'),
  persistenceEnabled: process.env.SANDBOX_PERSIST !== 'false',
  dataFile: path.resolve(__dirname, '..', process.env.SANDBOX_DATA_FILE || '.data/store.json'),
  // Which shared-mobility operator this instance simulates - see src/data/providers.js and
  // "Simulating different providers" in README.md.
  provider: process.env.SANDBOX_PROVIDER || 'gosharing',
};
