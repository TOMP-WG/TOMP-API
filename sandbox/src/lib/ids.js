const { randomUUID } = require('node:crypto');

const newOfferId = () => `offer-${randomUUID()}`;
const newPackageId = () => `package-${randomUUID()}`;
const newLegId = () => `leg-${randomUUID()}`;
const newPaymentId = () => randomUUID();

module.exports = { newOfferId, newPackageId, newLegId, newPaymentId };
