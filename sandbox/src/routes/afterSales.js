const { Router } = require('express');
const auth = require('../middleware/auth');
const store = require('../lib/store');
const { applyStandardHeaders, wrapPackage } = require('../lib/geojson');
const { TompError } = require('../lib/errors');

const router = Router();

router.post('/processes/cancel-package/execution', auth, (req, res, next) => {
  try {
    const packageId = req.body && req.body.inputs && req.body.inputs.package;
    if (!packageId) {
      throw new TompError({
        errorcode: 3,
        type: 'VALID',
        status: 400,
        instance: '/processes/cancel-package/execution',
        title: 'Missing inputs.package',
      });
    }
    const record = store.cancelPackage(packageId);
    applyStandardHeaders(res);
    res.status(200).type('application/geo+json').json(wrapPackage(record));
  } catch (err) {
    next(err);
  }
});

module.exports = router;
