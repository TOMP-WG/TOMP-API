const { Router } = require('express');
const auth = require('../middleware/auth');
const store = require('../lib/store');
const { applyStandardHeaders, wrapPackage } = require('../lib/geojson');
const { TompError } = require('../lib/errors');

const router = Router();

function requireInput(inputs, field, instance) {
  if (!inputs || !inputs[field]) {
    throw new TompError({
      errorcode: 3,
      type: 'VALID',
      status: 400,
      instance,
      title: `Missing inputs.${field}`,
    });
  }
  return inputs[field];
}

router.post('/processes/purchase-offers/execution', auth, (req, res, next) => {
  try {
    const inputs = req.body && req.body.inputs;
    const offerId = requireInput(inputs, 'offer', '/processes/purchase-offers/execution');
    const record = store.purchaseOffer({
      offerId,
      customer: inputs.customer,
      paymentMethod: inputs.paymentMethod,
      travellers: inputs.travellers,
    });
    applyStandardHeaders(res);
    res.status(200).type('application/geo+json').json(wrapPackage(record));
  } catch (err) {
    next(err);
  }
});

router.post('/processes/purchase-package/execution', auth, (req, res, next) => {
  try {
    const inputs = req.body && req.body.inputs;
    const packageId = requireInput(inputs, 'package', '/processes/purchase-package/execution');
    const record = store.purchasePackage(packageId);
    applyStandardHeaders(res);
    res.status(200).type('application/geo+json').json(wrapPackage(record));
  } catch (err) {
    next(err);
  }
});

router.post('/processes/extend-expiry-time/execution', auth, (req, res, next) => {
  try {
    const inputs = req.body && req.body.inputs;
    const packageId = requireInput(inputs, 'package', '/processes/extend-expiry-time/execution');
    const record = store.extendExpiryTime({ packageId, reason: inputs.reason });
    applyStandardHeaders(res);
    res.status(200).type('application/geo+json').json(wrapPackage(record));
  } catch (err) {
    next(err);
  }
});

router.post('/processes/confirm-purchase/execution', auth, (req, res, next) => {
  try {
    const inputs = req.body && req.body.inputs;
    const packageId = requireInput(inputs, 'package', '/processes/confirm-purchase/execution');
    const record = store.confirmPurchase(packageId);
    applyStandardHeaders(res);
    res.status(200).type('application/geo+json').json(wrapPackage(record));
  } catch (err) {
    next(err);
  }
});

router.post('/processes/rollback-purchase/execution', auth, (req, res, next) => {
  try {
    const inputs = req.body && req.body.inputs;
    const packageId = requireInput(inputs, 'package', '/processes/rollback-purchase/execution');
    const record = store.rollbackPurchase(packageId);
    applyStandardHeaders(res);
    res.status(200).type('application/geo+json').json(wrapPackage(record));
  } catch (err) {
    next(err);
  }
});

module.exports = router;
