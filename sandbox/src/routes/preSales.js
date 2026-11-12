const { Router } = require('express');
const auth = require('../middleware/auth');
const store = require('../lib/store');
const { applyStandardHeaders, wrapPackage } = require('../lib/geojson');
const { TompError } = require('../lib/errors');

const router = Router();

router.post('/processes/select-offers/execution', auth, (req, res, next) => {
  try {
    const inputs = req.body && req.body.inputs;
    const offerIds = inputs && inputs.offers;
    if (!Array.isArray(offerIds) || offerIds.length === 0) {
      throw new TompError({
        errorcode: 3,
        type: 'VALID',
        status: 400,
        instance: '/processes/select-offers/execution',
        title: 'Missing inputs.offers',
        detail: 'inputs.offers must be a non-empty array of offer ids',
      });
    }
    const record = store.selectOffers({ offerIds });
    applyStandardHeaders(res);
    res.status(200).type('application/geo+json').json(wrapPackage(record));
  } catch (err) {
    next(err);
  }
});

module.exports = router;
