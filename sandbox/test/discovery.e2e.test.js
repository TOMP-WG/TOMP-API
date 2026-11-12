process.env.SANDBOX_PERSIST = 'false'; // keep tests isolated from any real .data/store.json on disk

const test = require('node:test');
const assert = require('node:assert/strict');
const request = require('supertest');

const createApp = require('../src/app');

test('landing page links to conformance, api doc, collections and processes', async () => {
  const app = await createApp();
  const res = await request(app).get('/?f=json');
  assert.equal(res.status, 200);
  const rels = res.body.links.map((l) => l.rel);
  assert.ok(rels.includes('conformance'));
  assert.ok(rels.includes('service-desc'));
  assert.ok(rels.includes('data'));
});

test('conformance lists OGC API Features and Processes classes', async () => {
  const app = await createApp();
  const res = await request(app).get('/conformance?f=json');
  assert.equal(res.status, 200);
  assert.ok(res.body.conformsTo.some((c) => c.includes('ogcapi-features-1')));
  assert.ok(res.body.conformsTo.some((c) => c.includes('ogcapi-processes-1')));
});

test('discovery/metadata endpoints render HTML by default and json on request', async () => {
  const app = await createApp();
  for (const url of ['/', '/conformance', '/collections', '/collections/packages', '/processes', '/processes/confirm-purchase']) {
    const res = await request(app).get(url);
    assert.equal(res.status, 200, url);
    assert.match(res.type, /html/, url);
    assert.match(res.text, /<pre>/, url);
  }
});

test('/api renders an interactive Swagger UI by default (same as ?f=html)', async () => {
  const app = await createApp();
  for (const url of ['/api', '/api?f=html']) {
    const htmlRes = await request(app).get(url);
    assert.equal(htmlRes.status, 200);
    assert.match(htmlRes.type, /html/);
    assert.match(htmlRes.text, /SwaggerUIBundle/);
  }

  const assetRes = await request(app).get('/api-assets/swagger-ui-bundle.js');
  assert.equal(assetRes.status, 200);
});

test('/api?f=yaml serves the raw spec as text/plain (so browsers render it inline), ?f=json parsed as JSON', async () => {
  const app = await createApp();
  const yamlRes = await request(app).get('/api?f=yaml');
  assert.equal(yamlRes.status, 200);
  assert.match(yamlRes.type, /text\/plain/);
  assert.match(yamlRes.text, /^openapi: 3\.0\.0/);

  const jsonRes = await request(app).get('/api?f=json');
  assert.equal(jsonRes.status, 200);
  assert.equal(jsonRes.body.openapi, '3.0.0');
});

test('/collections lists only the collections this sandbox implements', async () => {
  const app = await createApp();
  const res = await request(app).get('/collections?f=json');
  assert.equal(res.status, 200);
  const ids = res.body.collections.map((c) => c.id);
  assert.deepEqual(ids.sort(), ['offers', 'packages', 'payments', 'travel-documents']);
});

test('/collections/:id describes a known collection and 404s an unknown one', async () => {
  const app = await createApp();
  const known = await request(app).get('/collections/packages?f=json');
  assert.equal(known.status, 200);
  assert.equal(known.body.id, 'packages');

  const unknown = await request(app).get('/collections/nonsense?f=json');
  assert.equal(unknown.status, 404);
});

test('/processes lists only implemented processes, each with a sync execute link', async () => {
  const app = await createApp();
  const res = await request(app).get('/processes?f=json');
  assert.equal(res.status, 200);
  const searchOffers = res.body.processes.find((p) => p.id === 'search-offers');
  assert.ok(searchOffers);
  assert.deepEqual(searchOffers.jobControlOptions, ['sync-execute']);
  assert.ok(searchOffers.links.some((l) => l.rel === 'execute' && l.href === '/processes/search-offers/execution'));
});

test('/processes/:id 200s an implemented process, 501s an out-of-scope one, 404s an unknown one', async () => {
  const app = await createApp();

  const implemented = await request(app).get('/processes/confirm-purchase?f=json');
  assert.equal(implemented.status, 200);

  const outOfScope = await request(app).get('/processes/postpone-leg');
  assert.equal(outOfScope.status, 501);
  assert.equal(outOfScope.body.errors[0].type, 'SCOPE');

  const unknown = await request(app).get('/processes/does-not-exist');
  assert.equal(unknown.status, 404);
});
