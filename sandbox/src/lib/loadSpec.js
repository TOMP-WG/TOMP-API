const fs = require('node:fs');
const path = require('node:path');
const os = require('node:os');
const crypto = require('node:crypto');

const config = require('../config');

// TOMP-API.yaml:5247 (placeReference.pattern) left a documentation placeholder inside the actual
// regex: "{datasource-prefix}" isn't valid regex syntax ("Lone quantifier brackets"). This is a
// pre-existing upstream spec defect, unrelated to any endpoint this sandbox implements. Rather than
// disabling request validation for the whole app, patch this one pattern in a cached copy so
// express-openapi-validator can still compile and validate against the rest of the spec untouched.
const BROKEN_PATTERN = '^(GPS|gps|{datasource-prefix}|P):[a-zA-Z0-9\\-_.]+$';
const FIXED_PATTERN = '^(GPS|gps|P):[a-zA-Z0-9\\-_.]+$';

function resolveValidatableSpecPath() {
  const original = fs.readFileSync(config.specPath, 'utf8');
  if (!original.includes(BROKEN_PATTERN)) {
    return config.specPath;
  }
  const patched = original.split(BROKEN_PATTERN).join(FIXED_PATTERN);
  const cacheDir = path.join(os.tmpdir(), 'tomp-api-sandbox');
  fs.mkdirSync(cacheDir, { recursive: true });
  const hash = crypto.createHash('sha1').update(config.specPath).digest('hex').slice(0, 8);
  const cachePath = path.join(cacheDir, `TOMP-API.patched.${hash}.yaml`);
  fs.writeFileSync(cachePath, patched, 'utf8');
  return cachePath;
}

module.exports = { resolveValidatableSpecPath };
