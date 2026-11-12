const { Router } = require('express');
const auth = require('../middleware/auth');
const store = require('../lib/store');
const { applyStandardHeaders, wrapPackage } = require('../lib/geojson');
const { TompError } = require('../lib/errors');

const router = Router();

// legStatus-changing operations implemented in this sandbox (see README "out of scope")
const IMPLEMENTED_OPERATIONS = new Set(['start', 'pause', 'resume', 'end']);
// valid per the spec's legOperation enum, but not implemented here
const OUT_OF_SCOPE_OPERATIONS = new Set(['extend', 'postpone']);

// path is literally "/processes/{legOperation}-leg/execution", e.g. /processes/start-leg/execution
router.post(/^\/processes\/([a-z]+)-leg\/execution$/, auth, (req, res, next) => {
  try {
    const legOperation = req.params[0];
    const instance = req.originalUrl;

    if (OUT_OF_SCOPE_OPERATIONS.has(legOperation)) {
      throw new TompError({
        errorcode: 9,
        type: 'SCOPE',
        status: 501,
        instance,
        title: 'Leg operation not implemented',
        detail: `${legOperation}-leg is out of scope for this sandbox`,
      });
    }
    if (!IMPLEMENTED_OPERATIONS.has(legOperation)) {
      throw new TompError({ errorcode: 2, type: 'NOTFOUND', status: 404, instance, title: 'Unknown leg operation' });
    }

    const inputs = req.body && req.body.inputs;
    if (!inputs || !inputs.leg) {
      throw new TompError({
        errorcode: 3,
        type: 'VALID',
        status: 400,
        instance,
        title: 'Missing inputs.leg',
      });
    }

    const record = store.legOperation({ legOperation, legId: inputs.leg, packageId: inputs.package });
    applyStandardHeaders(res);
    res.status(200).type('application/geo+json').json(wrapPackage(record));
  } catch (err) {
    next(err);
  }
});

module.exports = router;
