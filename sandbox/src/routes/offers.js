const { Router } = require('express');
const auth = require('../middleware/auth');
const store = require('../lib/store');
const { applyStandardHeaders, wrapOfferCollection, wrapPackage } = require('../lib/geojson');
const { TompError } = require('../lib/errors');

const router = Router();

router.post('/processes/search-offers/execution', auth, (req, res, next) => {
  try {
    const inputs = req.body && req.body.inputs;
    if (!inputs || !inputs.specification) {
      throw new TompError({
        errorcode: 3,
        type: 'VALID',
        status: 400,
        title: 'Missing specification',
        detail: 'inputs.specification is required',
      });
    }
    const offerRecords = store.searchOffers({ specification: inputs.specification, travellers: inputs.travellers });
    applyStandardHeaders(res);
    res.set('Expires', new Date(Date.now() + 15 * 60 * 1000).toUTCString());
    res.status(200).type('application/geo+json').json(wrapOfferCollection(offerRecords));
  } catch (err) {
    next(err);
  }
});

router.get('/collections/offers/items', auth, (req, res, next) => {
  try {
    const { offerId } = req.query;
    const record = store.getOffer(offerId);
    applyStandardHeaders(res);
    res.status(200).type('application/geo+json').json(wrapPackage(record));
  } catch (err) {
    next(err);
  }
});

module.exports = router;
