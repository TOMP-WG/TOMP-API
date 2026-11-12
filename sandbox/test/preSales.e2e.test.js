process.env.SANDBOX_PERSIST = 'false'; // keep tests isolated from any real .data/store.json on disk
process.env.SANDBOX_PROVIDER = 'uber'; // taxi provider -> its vehicle offer carries bookingFlow: 'select'

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

test('offer results link walking/shared offers to purchase-offers and taxi offers to select-offers', async () => {
  const app = await createApp();
  const token = await getToken(app);
  const auth = (req) => req.set('Authorization', `Bearer ${token}`).set('Accept-Language', 'en-US');

  const search = await auth(request(app).post('/processes/search-offers/execution')).send({
    inputs: {
      type: 'searchOffer',
      specification: { type: 'travel_specification', from: 'gps:52.3791,4.9003', to: 'gps:52.3550,4.8900' },
    },
  });
  assert.equal(search.status, 200);
  assert.equal(search.body.features.length, 2);

  const footOffer = search.body.features.find((f) => f.properties.legs[0].mode === 'FOOT');
  const taxiOffer = search.body.features.find((f) => f.properties.legs[0].mode === 'TAXI');
  assert.ok(footOffer && taxiOffer);

  assert.ok(footOffer.links.some((l) => l.rel === 'purchase-offers' && l.method === 'POST'));
  assert.ok(!footOffer.links.some((l) => l.rel === 'select-offers'));

  assert.ok(taxiOffer.links.some((l) => l.rel === 'select-offers' && l.method === 'POST'));
  assert.ok(!taxiOffer.links.some((l) => l.rel === 'purchase-offers'));

  const select = await auth(request(app).post('/processes/select-offers/execution')).send({
    inputs: { offers: [taxiOffer.id] },
  });
  assert.equal(select.status, 200);
  assert.equal(select.body.properties.status, 'PENDING');
  assert.ok(select.body.links.some((l) => l.rel === 'purchase-package' && l.method === 'POST'));
  assert.ok(!select.body.links.some((l) => ['confirm-purchase', 'rollback-purchase'].includes(l.rel)));
  const packageId = select.body.properties.id;

  // A merely-selected (reserved, not yet purchased) package can't be confirmed directly.
  const prematureConfirm = await auth(request(app).post('/processes/confirm-purchase/execution')).send({
    inputs: { package: packageId },
  });
  assert.equal(prematureConfirm.status, 409);
  assert.equal(prematureConfirm.body.errors[0].type, 'STATE');

  const purchase = await auth(request(app).post('/processes/purchase-package/execution')).send({
    inputs: { package: packageId },
  });
  assert.equal(purchase.status, 200);
  assert.equal(purchase.body.properties.status, 'PENDING');
  assert.ok(purchase.body.links.some((l) => l.rel === 'confirm-purchase' && l.method === 'POST'));
  assert.ok(purchase.body.links.some((l) => l.rel === 'extend-expiry-time' && l.method === 'POST'));
  assert.ok(purchase.body.links.some((l) => l.rel === 'rollback-purchase' && l.method === 'POST'));
  assert.ok(!purchase.body.links.some((l) => l.rel === 'purchase-package'));

  const extend = await auth(request(app).post('/processes/extend-expiry-time/execution')).send({
    inputs: { package: packageId, reason: 'PAYMENT_PENDING' },
  });
  assert.equal(extend.status, 200);
  assert.equal(extend.body.properties.status, 'PENDING');

  // Travel documents aren't available before the package is actually CONFIRMED.
  const tooEarly = await auth(request(app).get(`/collections/travel-documents/items?packageId=${packageId}`));
  assert.equal(tooEarly.status, 409);

  const confirm = await auth(request(app).post('/processes/confirm-purchase/execution')).send({
    inputs: { package: packageId },
  });
  assert.equal(confirm.status, 200);
  assert.equal(confirm.body.properties.status, 'CONFIRMED');
  assert.ok(confirm.body.links.some((l) => l.rel === 'cancel-package' && l.method === 'POST'));
  assert.ok(confirm.body.links.some((l) => l.rel === 'travel-documents' && l.method === 'GET'));

  const documents = await auth(request(app).get(`/collections/travel-documents/items?packageId=${packageId}`));
  assert.equal(documents.status, 200);
  assert.equal(documents.body.features.length, 1);
  assert.equal(documents.body.features[0].properties.travelDocumentType, 'BARCODE');
  assert.ok(documents.body.features[0].links.some((l) => l.rel === 'boarding-code'));
});

test('select-offers 400s without inputs.offers', async () => {
  const app = await createApp();
  const token = await getToken(app);
  const res = await request(app)
    .post('/processes/select-offers/execution')
    .set('Authorization', `Bearer ${token}`)
    .set('Accept-Language', 'en-US')
    .send({ inputs: {} });
  assert.equal(res.status, 400);
});
