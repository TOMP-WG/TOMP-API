const { Router } = require('express');
const auth = require('../middleware/auth');
const store = require('../lib/store');
const { applyStandardHeaders, wrapPackage, wrapTravelDocuments } = require('../lib/geojson');

const router = Router();

router.get('/collections/packages/items', auth, (req, res, next) => {
  try {
    const { packageId } = req.query;
    const record = store.getPackage(packageId);
    applyStandardHeaders(res);
    res.status(200).type('application/geo+json').json(wrapPackage(record));
  } catch (err) {
    next(err);
  }
});

router.get('/collections/travel-documents/items', auth, (req, res, next) => {
  try {
    const { packageId } = req.query;
    const documents = store.getTravelDocuments(packageId);
    applyStandardHeaders(res);
    res.status(200).type('application/geo+json').json(wrapTravelDocuments(documents, packageId));
  } catch (err) {
    next(err);
  }
});

module.exports = router;
