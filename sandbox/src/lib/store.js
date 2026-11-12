const fs = require('node:fs');
const path = require('node:path');

const { newOfferId, newPackageId, newLegId, newPaymentId } = require('./ids');
const { TompError } = require('./errors');
const { assertPackageTransition, assertLegTransition } = require('./stateMachine');
const { resolveProvider, findNearestVehicle } = require('../data/providers');
const config = require('../config');

// Registry kept in memory and mirrored to a JSON dump on every mutation - see "Persistence" in
// sandbox/README.md. Disable with SANDBOX_PERSIST=false (e.g. in tests) to stay purely in-memory.
const offers = new Map(); // offerId -> { properties, legs: Map<legId, legProperties>, createdAt, expiresAt }
const packages = new Map(); // packageId -> { properties, legs: Map<legId, legProperties>, history, customer, paymentMethod }
const payments = new Map(); // paymentId -> financialDetail-ish record

const OFFER_TTL_MS = 15 * 60 * 1000;
const ROLLBACK_WINDOW_MS = 10 * 60 * 1000;

// Which operator this running instance simulates - fixed for the process lifetime, so starting
// the sandbox again with a different SANDBOX_PROVIDER simulates a different operator.
const activeProvider = resolveProvider(config.provider);

// Walking is always available, operator-agnostic. The active provider's own mode (shared
// bicycle/moped, or taxi) is added on top of that, but only for searches whose `from` falls
// within one of that provider's seeded Amsterdam/Utrecht coverage areas - see
// src/data/providers.js. That makes "no offer for this operator here" a realistic outcome, not a
// bug: e.g. a taxi-only provider never produces a BICYCLE offer, and a provider that only covers
// Amsterdam has nothing near Utrecht.
function buildOfferVariants(specification) {
  const variants = [
    {
      mode: 'FOOT',
      label: 'Walking route',
      basePrice: 0,
      operatorName: 'TOMP Sandbox Transport Operator',
      product: 'product-sandbox-foot',
      // Self-service modes (walking, shared bicycle/moped) can be purchased straight away; a
      // dispatched ride (taxi) has to be reserved with select-offers first - see "Offer links"
      // in README.md.
      bookingFlow: 'direct',
    },
  ];

  const match = specification && findNearestVehicle(activeProvider, specification.from);
  if (match) {
    const { vehicle, city } = match;
    const { mode, name, pricing } = activeProvider;
    variants.push({
      mode,
      label: `${name} ${mode === 'TAXI' ? 'taxi' : 'shared ' + mode.toLowerCase()} (${city.name})`,
      basePrice: pricing.basePrice,
      operatorName: name,
      product: `product-${vehicle.id}`,
      bookingFlow: mode === 'TAXI' ? 'select' : 'direct',
    });
  }

  return variants;
}

// offers and packages share the same shape (a `legs: Map<legId, legProperties>` plus plain fields)
function serializeRecord(record) {
  return { ...record, legs: Object.fromEntries(record.legs) };
}

function deserializeRecord(data) {
  return { ...data, legs: new Map(Object.entries(data.legs || {})) };
}

function persist() {
  if (!config.persistenceEnabled) return;
  const dump = {
    offers: Object.fromEntries([...offers].map(([id, record]) => [id, serializeRecord(record)])),
    packages: Object.fromEntries([...packages].map(([id, record]) => [id, serializeRecord(record)])),
    payments: Object.fromEntries(payments),
  };
  fs.mkdirSync(path.dirname(config.dataFile), { recursive: true });
  fs.writeFileSync(config.dataFile, JSON.stringify(dump, null, 2));
}

function loadFromDisk() {
  if (!config.persistenceEnabled || !fs.existsSync(config.dataFile)) return;
  try {
    const dump = JSON.parse(fs.readFileSync(config.dataFile, 'utf8'));
    for (const [id, data] of Object.entries(dump.offers || {})) offers.set(id, deserializeRecord(data));
    for (const [id, data] of Object.entries(dump.packages || {})) packages.set(id, deserializeRecord(data));
    for (const [id, data] of Object.entries(dump.payments || {})) payments.set(id, data);
  } catch (err) {
    console.error(`Failed to load ${config.dataFile}, starting with an empty store:`, err.message);
  }
}

function recordHistory(record, entry) {
  record.history.push({ at: new Date().toISOString(), ...entry });
}

function buildLegProperties({ legId, specification, travellers, variant }) {
  return {
    type: 'leg',
    id: legId,
    specification,
    sequenceNumber: 1,
    mode: variant.mode,
    status: 'NOT_STARTED',
    travellers: (travellers || []).map((t) => t.id).filter(Boolean),
    products: [variant.product],
    operatorName: variant.operatorName,
  };
}

function createOfferRecord({ specification, travellers, variant }) {
  const offerId = newOfferId();
  const legId = newLegId();
  const amount = Number((variant.basePrice + Math.random() * 3).toFixed(2));
  const legProperties = buildLegProperties({ legId, specification, travellers, variant });
  const price = { amount, currencyCode: 'EUR', elements: [] };
  const properties = {
    type: 'offer',
    id: offerId,
    status: 'OFFERED',
    price,
    bookingFlow: variant.bookingFlow,
    legs: [legProperties],
    summary: {
      id: offerId,
      specification,
      price,
      estimatedPrice: false,
      products: legProperties.products,
      legs: [{ mode: variant.mode, name: variant.label, destination: specification && specification.to }],
    },
  };
  const record = {
    properties,
    legs: new Map([[legId, legProperties]]),
    createdAt: Date.now(),
    expiresAt: Date.now() + OFFER_TTL_MS,
  };
  offers.set(offerId, record);
  return record;
}

function searchOffers({ specification, travellers }) {
  const records = buildOfferVariants(specification).map((variant) =>
    createOfferRecord({ specification, travellers, variant }),
  );
  persist();
  return records;
}

function getOffer(offerId) {
  const record = offers.get(offerId);
  if (!record) {
    throw new TompError({
      errorcode: 2,
      type: 'NOTFOUND',
      status: 404,
      title: 'Offer not found',
      detail: `No offer with id ${offerId}`,
    });
  }
  return record;
}

function getPackage(packageId) {
  const record = packages.get(packageId);
  if (!record) {
    throw new TompError({
      errorcode: 2,
      type: 'NOTFOUND',
      status: 404,
      title: 'Package not found',
      detail: `No package with id ${packageId}`,
    });
  }
  return record;
}

function syncPackageLegs(record) {
  record.properties.legs = [...record.legs.values()];
}

function purchaseOffer({ offerId, customer, paymentMethod, travellers }) {
  const offerRecord = getOffer(offerId);
  const packageId = newPackageId();
  const legs = new Map();
  for (const [legId, legProperties] of offerRecord.legs) {
    legs.set(legId, { ...legProperties });
  }

  const properties = {
    ...offerRecord.properties,
    type: 'package',
    id: packageId,
    status: 'PENDING',
    legs: [...legs.values()],
  };

  const record = {
    properties,
    legs,
    history: [],
    customer: customer || null,
    paymentMethod: paymentMethod || null,
    // Distinguishes this fully-purchased package from one only reserved via selectOffers below -
    // both can be status PENDING, but only the latter still needs a purchase-package call; see
    // packageActionLinks in lib/geojson.js.
    purchaseStage: 'purchased',
    rollbackExpiresAt: Date.now() + ROLLBACK_WINDOW_MS,
  };
  recordHistory(record, { operation: 'purchase-offers', from: null, to: 'PENDING' });

  packages.set(packageId, record);
  offers.delete(offerId); // an offer is consumed by a single purchase

  persist();
  return record;
}

// Pre-sales equivalent of purchaseOffer: reserves one or more offers into a single PENDING
// package without purchasing them outright - used by modes whose offer carries
// `bookingFlow: 'select'` (e.g. a dispatched taxi ride that must be requested before it's bought).
function selectOffers({ offerIds }) {
  const offerRecords = offerIds.map((offerId) => getOffer(offerId));
  const packageId = newPackageId();
  const legs = new Map();
  for (const offerRecord of offerRecords) {
    for (const [legId, legProperties] of offerRecord.legs) {
      legs.set(legId, { ...legProperties });
    }
  }

  const price = offerRecords.reduce(
    (total, offerRecord) => ({
      amount: Number((total.amount + offerRecord.properties.price.amount).toFixed(2)),
      currencyCode: offerRecord.properties.price.currencyCode,
      elements: [],
    }),
    { amount: 0, currencyCode: 'EUR', elements: [] },
  );

  const properties = {
    type: 'package',
    id: packageId,
    status: 'PENDING',
    price,
    legs: [...legs.values()],
  };

  const record = {
    properties,
    legs,
    history: [],
    customer: null,
    paymentMethod: null,
    // 'selected' means reserved but not yet purchased - purchasePackage below flips this to
    // 'purchased', which is when the usual confirm/extend/rollback links start applying.
    purchaseStage: 'selected',
    rollbackExpiresAt: Date.now() + ROLLBACK_WINDOW_MS,
  };
  recordHistory(record, { operation: 'select-offers', from: null, to: 'PENDING' });

  packages.set(packageId, record);
  for (const offerId of offerIds) offers.delete(offerId); // selected offers are consumed

  persist();
  return record;
}

// Purchases a package that was only reserved via selectOffers (e.g. a taxi ride still has to be
// accepted by a driver) - status stays PENDING, same as a direct purchaseOffer, but purchaseStage
// flips to 'purchased' so it now gets the regular confirm/extend/rollback links instead of
// purchase-package again.
function purchasePackage(packageId) {
  const record = getPackage(packageId);
  const instance = '/processes/purchase-package/execution';
  if (record.purchaseStage !== 'selected' || record.properties.status !== 'PENDING') {
    throw new TompError({
      errorcode: 1,
      type: 'STATE',
      status: 409,
      instance,
      title: 'Package is not a pending selection',
      detail: `Package ${packageId} wasn't created by select-offers, or was already purchased`,
    });
  }
  record.purchaseStage = 'purchased';
  recordHistory(record, { operation: 'purchase-package', from: 'PENDING', to: 'PENDING' });
  persist();
  return record;
}

// Requests more time before rollbackExpiresAt runs out, without changing the package's status -
// only valid while still PENDING (OFFERED/CONFIRMED/etc have nothing left to extend).
function extendExpiryTime({ packageId, reason }) {
  const record = getPackage(packageId);
  const instance = '/processes/extend-expiry-time/execution';
  if (record.properties.status !== 'PENDING') {
    throw new TompError({
      errorcode: 1,
      type: 'STATE',
      status: 409,
      instance,
      title: 'Package is not pending',
      detail: `Can only extend the expiry time of a PENDING package (currently ${record.properties.status})`,
    });
  }
  record.rollbackExpiresAt = Date.now() + ROLLBACK_WINDOW_MS;
  recordHistory(record, { operation: 'extend-expiry-time', from: 'PENDING', to: 'PENDING', reason: reason || null });
  persist();
  return record;
}

// A travelDocumentType per TOMP-API-1-CORE.yaml's enum, picked by leg mode: FOOT needs no
// document at all (REMOTE - start-leg is enough), a shared vehicle needs unlock data (DEEP_LINK),
// a taxi needs a boarding code to show the driver (BARCODE).
function travelDocumentTypeForMode(mode) {
  if (mode === 'FOOT') return 'REMOTE';
  if (mode === 'TAXI') return 'BARCODE';
  return 'DEEP_LINK';
}

function travelDocumentLink(mode, legId) {
  if (mode === 'FOOT') return null;
  if (mode === 'TAXI') {
    return {
      rel: 'boarding-code',
      href: `sandbox://boarding/${legId}`,
      description: 'Show this code to the driver to board',
      body: { code: legId.slice(-6).toUpperCase() },
    };
  }
  return {
    rel: 'unlock-data',
    href: `sandbox://unlock/${legId}`,
    description: 'Deep link / PIN to unlock the vehicle',
    body: { deepLink: `sandbox-rider://unlock/${legId}`, pin: legId.slice(-4) },
  };
}

// Only meaningful once a package is actually confirmed (or further along) - see
// packageActionLinks in lib/geojson.js for when the travel-documents link is shown at all.
const TRAVEL_DOCUMENT_ELIGIBLE_STATUSES = new Set(['CONFIRMED', 'STARTED', 'ENDED', 'SETTLED']);

function getTravelDocuments(packageId) {
  const record = getPackage(packageId);
  if (!TRAVEL_DOCUMENT_ELIGIBLE_STATUSES.has(record.properties.status)) {
    throw new TompError({
      errorcode: 1,
      type: 'STATE',
      status: 409,
      instance: '/collections/travel-documents/items',
      title: 'Package not confirmed yet',
      detail: `Travel documents are only available once a package is CONFIRMED (currently ${record.properties.status})`,
    });
  }
  const now = Date.now();
  return [...record.legs.values()].map((leg) => ({
    id: `traveldoc-${leg.id}`,
    type: 'travelDocument',
    package: packageId,
    leg: leg.id,
    travelDocumentType: travelDocumentTypeForMode(leg.mode),
    validity: [new Date(now).toISOString(), new Date(now + 24 * 60 * 60 * 1000).toISOString()],
    link: travelDocumentLink(leg.mode, leg.id),
  }));
}

function confirmPurchase(packageId) {
  const record = getPackage(packageId);
  const instance = '/processes/confirm-purchase/execution';
  if (record.purchaseStage === 'selected') {
    throw new TompError({
      errorcode: 1,
      type: 'STATE',
      status: 409,
      instance,
      title: 'Package not purchased yet',
      detail: `Package ${packageId} was only reserved via select-offers - call purchase-package first`,
    });
  }
  const from = record.properties.status;
  const next = assertPackageTransition(from, 'confirmPurchase', instance);
  record.properties.status = next;
  recordHistory(record, { operation: 'confirm-purchase', from, to: next });
  generatePaymentForPackage(record);
  persist();
  return record;
}

function rollbackPurchase(packageId) {
  const record = getPackage(packageId);
  const from = record.properties.status;
  const next = assertPackageTransition(from, 'rollbackPurchase', '/processes/rollback-purchase/execution');
  record.properties.status = next;
  recordHistory(record, { operation: 'rollback-purchase', from, to: next });
  persist();
  return record;
}

function cancelPackage(packageId) {
  const record = getPackage(packageId);
  const from = record.properties.status;
  const next = assertPackageTransition(from, 'cancelPackage', '/processes/cancel-package/execution');
  record.properties.status = next;
  recordHistory(record, { operation: 'cancel-package', from, to: next });
  persist();
  return record;
}

function findPackageIdForLeg(legId) {
  for (const [packageId, record] of packages) {
    if (record.legs.has(legId)) return packageId;
  }
  throw new TompError({
    errorcode: 2,
    type: 'NOTFOUND',
    status: 404,
    title: 'Leg not found',
    detail: `No leg with id ${legId} in any package`,
  });
}

function legOperation({ legOperation: operation, legId, packageId }) {
  const resolvedPackageId = packageId || findPackageIdForLeg(legId);
  const record = getPackage(resolvedPackageId);
  const instance = `/processes/${operation}-leg/execution`;
  const leg = record.legs.get(legId);
  if (!leg) {
    throw new TompError({
      errorcode: 2,
      type: 'NOTFOUND',
      status: 404,
      instance,
      title: 'Leg not found',
      detail: `No leg ${legId} in package ${resolvedPackageId}`,
    });
  }

  if (operation === 'start' && !['CONFIRMED', 'STARTED'].includes(record.properties.status)) {
    throw new TompError({
      errorcode: 1,
      type: 'STATE',
      status: 409,
      instance,
      title: 'Package not ready to start a leg',
      detail: `Package must be CONFIRMED before starting a leg (currently ${record.properties.status})`,
    });
  }

  const from = leg.status;
  const next = assertLegTransition(from, operation, instance);
  leg.status = next;
  recordHistory(record, { operation: `${operation}-leg`, legId, from, to: next });

  if (operation === 'start' && record.properties.status === 'CONFIRMED') {
    record.properties.status = 'STARTED';
    recordHistory(record, { operation: 'derived', from: 'CONFIRMED', to: 'STARTED' });
  }

  if (operation === 'end') {
    const allLegsEnded = [...record.legs.values()].every((l) => ['ENDED', 'CANCELLED', 'ABENDED'].includes(l.status));
    if (allLegsEnded && record.properties.status === 'STARTED') {
      record.properties.status = 'ENDED';
      recordHistory(record, { operation: 'derived', from: 'STARTED', to: 'ENDED' });
    }
  }

  syncPackageLegs(record);
  persist();
  return record;
}

function generatePaymentForPackage(record) {
  const amount = record.properties.price ? record.properties.price.amount : 0;
  const paymentId = newPaymentId();
  const payment = {
    id: paymentId,
    packageId: record.properties.id,
    amount,
    currencyCode: 'EUR',
    category: 'FARE',
    state: 'TO_INVOICE',
    createdAt: new Date().toISOString(),
  };
  payments.set(paymentId, payment);
  return payment;
}

function listPayments({ packageId, invoiceState, category }) {
  return [...payments.values()].filter(
    (p) =>
      (!packageId || p.packageId === packageId) &&
      (!invoiceState || p.state === invoiceState) &&
      (!category || p.category === category),
  );
}

function confirmPayment(paymentId) {
  const payment = payments.get(paymentId);
  if (!payment) {
    throw new TompError({
      errorcode: 2,
      type: 'NOTFOUND',
      status: 404,
      title: 'Payment not found',
      detail: `No payment with id ${paymentId}`,
    });
  }
  payment.state = 'INVOICED';

  const record = packages.get(payment.packageId);
  if (record) {
    const allInvoiced = [...payments.values()]
      .filter((p) => p.packageId === record.properties.id)
      .every((p) => p.state === 'INVOICED');
    if (allInvoiced && record.properties.status === 'ENDED') {
      record.properties.status = 'SETTLED';
      recordHistory(record, { operation: 'derived', from: 'ENDED', to: 'SETTLED' });
    }
  }
  persist();
  return payment;
}

module.exports = {
  searchOffers,
  getOffer,
  getPackage,
  purchaseOffer,
  selectOffers,
  purchasePackage,
  extendExpiryTime,
  getTravelDocuments,
  confirmPurchase,
  rollbackPurchase,
  cancelPackage,
  legOperation,
  listPayments,
  confirmPayment,
  loadFromDisk,
};
