process.env.SANDBOX_PERSIST = 'false'; // keep tests isolated from any real .data/store.json on disk

const test = require('node:test');
const assert = require('node:assert/strict');
const request = require('supertest');

const createApp = require('../src/app');

async function getToken(app) {
  const res = await request(app)
    .post('/oauth/token')
    .type('form')
    .send({ grant_type: 'client_credentials', client_id: 'test', client_secret: 'test' });
  assert.equal(res.status, 200);
  return res.body.access_token;
}

test('full package lifecycle: search -> purchase -> confirm -> start -> end -> pay -> settle', async () => {
  const app = await createApp();
  const token = await getToken(app);
  const auth = (req) => req.set('Authorization', `Bearer ${token}`).set('Accept-Language', 'en-US');

  const search = await auth(request(app).post('/processes/search-offers/execution')).send({
    inputs: {
      type: 'searchOffer',
      specification: { type: 'travel_specification', from: 'gps:52.0,4.3', to: 'gps:52.1,4.4' },
    },
  });
  assert.equal(search.status, 200);
  assert.ok(search.body.features.length >= 1);
  const offerId = search.body.features[0].id;

  const purchase = await auth(request(app).post('/processes/purchase-offers/execution')).send({
    inputs: { offer: offerId },
  });
  assert.equal(purchase.status, 200);
  assert.equal(purchase.body.properties.status, 'PENDING');
  assert.ok(purchase.body.links.some((l) => l.rel === 'confirm-purchase'));
  assert.ok(purchase.body.links.some((l) => l.rel === 'extend-expiry-time'));
  assert.ok(purchase.body.links.some((l) => l.rel === 'rollback-purchase'));
  const packageId = purchase.body.properties.id;
  const legId = purchase.body.features[0].id;

  const confirm = await auth(request(app).post('/processes/confirm-purchase/execution')).send({
    inputs: { package: packageId },
  });
  assert.equal(confirm.status, 200);
  assert.equal(confirm.body.properties.status, 'CONFIRMED');
  assert.ok(confirm.body.links.some((l) => l.rel === 'cancel-package'));
  assert.ok(confirm.body.links.some((l) => l.rel === 'travel-documents'));

  const start = await auth(request(app).post('/processes/start-leg/execution')).send({
    inputs: { leg: legId, package: packageId },
  });
  assert.equal(start.status, 200);
  assert.equal(start.body.properties.status, 'STARTED');
  assert.equal(start.body.features[0].properties.status, 'IN_USE');

  const end = await auth(request(app).post('/processes/end-leg/execution')).send({
    inputs: { leg: legId, package: packageId },
  });
  assert.equal(end.status, 200);
  assert.equal(end.body.properties.status, 'ENDED');

  const payments = await auth(request(app).get(`/collections/payments/items?package=${packageId}`));
  assert.equal(payments.status, 200);
  assert.equal(payments.body.features.length, 1);
  const paymentId = payments.body.features[0].id;

  const confirmPayment = await auth(request(app).post('/processes/confirm-payment/execution')).send({
    inputs: { paymentId },
  });
  assert.equal(confirmPayment.status, 204);

  const settled = await auth(request(app).get(`/collections/packages/items?packageId=${packageId}`));
  assert.equal(settled.status, 200);
  assert.equal(settled.body.properties.status, 'SETTLED');

  const invalidRepeat = await auth(request(app).post('/processes/confirm-purchase/execution')).send({
    inputs: { package: packageId },
  });
  assert.equal(invalidRepeat.status, 409);
  assert.equal(invalidRepeat.body.errors[0].type, 'STATE');
});

test('rejects requests without a bearer token', async () => {
  const app = await createApp();
  const res = await request(app)
    .post('/processes/search-offers/execution')
    .set('Accept-Language', 'en-US')
    .send({ inputs: { type: 'searchOffer', specification: { type: 'travel_specification' } } });
  assert.equal(res.status, 401);
});

test('rejects unknown package ids with 404', async () => {
  const app = await createApp();
  const token = await getToken(app);
  const res = await request(app)
    .get('/collections/packages/items?packageId=does-not-exist')
    .set('Authorization', `Bearer ${token}`)
    .set('Accept-Language', 'en-US');
  assert.equal(res.status, 404);
});
