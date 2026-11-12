const { TompError } = require('./errors');

// packageStatus enum: TOMP-API-1-CORE.yaml:448-457
const PACKAGE_TRANSITIONS = {
  OFFERED: {},
  PENDING: { confirmPurchase: 'CONFIRMED', rollbackPurchase: 'ROLLBACK' },
  CONFIRMED: { rollbackPurchase: 'ROLLBACK', cancelPackage: 'CANCELLED' },
  STARTED: { cancelPackage: 'CANCELLED' },
  ROLLBACK: {},
  RELEASED: {},
  EXPIRED: {},
  CANCELLED: {},
  ENDED: {},
  SETTLED: {},
};

// legStatus enum: TOMP-API-1-CORE.yaml:474-482 (note: ENDING is narrative-only, not in the enum)
const LEG_TRANSITIONS = {
  NOT_STARTED: { start: 'IN_USE' },
  PREPARING: {},
  READY_TO_USE: {},
  IN_USE: { pause: 'PAUSED', end: 'ENDED' },
  PAUSED: { resume: 'IN_USE', end: 'ENDED' },
  ENDED: {},
  ISSUE_REPORTED: {},
  CANCELLED: {},
  ABENDED: {},
};

function assertPackageTransition(status, trigger, instance) {
  const next = (PACKAGE_TRANSITIONS[status] || {})[trigger];
  if (!next) {
    throw new TompError({
      errorcode: 1,
      type: 'STATE',
      status: 409,
      instance,
      title: 'Invalid package state transition',
      detail: `Cannot ${trigger} a package in status ${status}`,
    });
  }
  return next;
}

function assertLegTransition(status, trigger, instance) {
  const next = (LEG_TRANSITIONS[status] || {})[trigger];
  if (!next) {
    throw new TompError({
      errorcode: 1,
      type: 'STATE',
      status: 409,
      instance,
      title: 'Invalid leg state transition',
      detail: `Cannot ${trigger} a leg in status ${status}`,
    });
  }
  return next;
}

module.exports = {
  PACKAGE_TRANSITIONS,
  LEG_TRANSITIONS,
  assertPackageTransition,
  assertLegTransition,
};
