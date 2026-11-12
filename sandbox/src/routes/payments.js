const { Router } = require('express');
const auth = require('../middleware/auth');
const store = require('../lib/store');
const { applyStandardHeaders, wrapPayments } = require('../lib/geojson');
const { TompError } = require('../lib/errors');

const router = Router();

router.get('/collections/payments/items', auth, (req, res, next) => {
  try {
    const { package: packageId, invoiceState, category } = req.query;
    const list = store.listPayments({ packageId, invoiceState, category });
    applyStandardHeaders(res);
    res.status(200).type('application/geo+json').json(wrapPayments(list, { package: packageId, invoiceState, category }));
  } catch (err) {
    next(err);
  }
});

router.post('/processes/confirm-payment/execution', auth, (req, res, next) => {
  try {
    const paymentId = req.body && req.body.inputs && req.body.inputs.paymentId;
    if (!paymentId) {
      throw new TompError({
        errorcode: 3,
        type: 'VALID',
        status: 400,
        instance: '/processes/confirm-payment/execution',
        title: 'Missing inputs.paymentId',
      });
    }
    store.confirmPayment(paymentId);
    res.status(204).end();
  } catch (err) {
    next(err);
  }
});

module.exports = router;
