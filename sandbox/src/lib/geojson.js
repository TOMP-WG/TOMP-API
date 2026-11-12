function applyStandardHeaders(res, { contentLanguage = 'en-US', version = '2.0.0' } = {}) {
  res.set('Version', version);
  res.set('Content-Language', contentLanguage);
}

// Which action links a package exposes next depends on its status - and, while PENDING, on
// whether it was reserved via select-offers and still needs purchase-package, or was already
// purchased (directly, or via purchase-package) and now just needs confirm/extend/rollback.
function packageActionLinks(record) {
  const id = record.properties.id;
  const status = record.properties.status;

  if (status === 'PENDING' && record.purchaseStage === 'selected') {
    return [
      {
        rel: 'purchase-package',
        href: '/processes/purchase-package/execution',
        method: 'POST',
        description: 'Purchase this previously selected (reserved) package',
        body: { inputs: { package: id } },
      },
    ];
  }

  if (status === 'PENDING') {
    return [
      {
        rel: 'confirm-purchase',
        href: '/processes/confirm-purchase/execution',
        method: 'POST',
        description: 'Confirm this pending purchase',
        body: { inputs: { package: id } },
      },
      {
        rel: 'extend-expiry-time',
        href: '/processes/extend-expiry-time/execution',
        method: 'POST',
        description: 'Request more time before this pending purchase expires',
        body: { inputs: { package: id } },
      },
      {
        rel: 'rollback-purchase',
        href: '/processes/rollback-purchase/execution',
        method: 'POST',
        description: 'Roll back this pending purchase, free of charge',
        body: { inputs: { package: id } },
      },
    ];
  }

  if (status === 'CONFIRMED') {
    return [
      {
        rel: 'cancel-package',
        href: '/processes/cancel-package/execution',
        method: 'POST',
        description: 'Cancel this confirmed package',
        body: { inputs: { package: id } },
      },
      {
        rel: 'travel-documents',
        href: `/collections/travel-documents/items?packageId=${id}`,
        method: 'GET',
        description: 'Travel documents for this package, e.g. unlock data to open a vehicle',
      },
    ];
  }

  return [];
}

function wrapPackage(record) {
  const legs = [...record.legs.values()];
  return {
    type: 'FeatureCollection',
    id: record.properties.id,
    features: legs.map((leg) => ({
      type: 'Feature',
      id: leg.id,
      properties: leg,
      links: [],
    })),
    properties: record.properties,
    numberMatched: legs.length,
    numberReturned: legs.length,
    links: [
      { rel: 'self', href: `/collections/packages/items?packageId=${record.properties.id}` },
      ...packageActionLinks(record),
    ],
  };
}

// Self-service offers (walking, shared bicycle/moped) link straight to purchase-offers; a
// dispatched ride (bookingFlow: 'select', e.g. taxi) links to select-offers instead, which
// reserves it into a PENDING package without purchasing it outright - see "Offer links" in
// README.md.
function offerActionLink(record) {
  if (record.properties.bookingFlow === 'select') {
    return {
      rel: 'select-offers',
      href: '/processes/select-offers/execution',
      method: 'POST',
      description: 'Reserve this offer into a PENDING package before purchasing it',
      body: { inputs: { offers: [record.properties.id] } },
    };
  }
  return {
    rel: 'purchase-offers',
    href: '/processes/purchase-offers/execution',
    method: 'POST',
    description: 'Purchase this offer directly',
    body: { inputs: { offer: record.properties.id } },
  };
}

function wrapOfferCollection(offerRecords) {
  return {
    type: 'FeatureCollection',
    features: offerRecords.map((record) => ({
      type: 'Feature',
      id: record.properties.id,
      properties: record.properties.summary,
      links: [
        { rel: 'self', href: `/collections/offers/items?offerId=${record.properties.id}` },
        offerActionLink(record),
      ],
    })),
    properties: { type: 'OfferCollection' },
    numberMatched: offerRecords.length,
    numberReturned: offerRecords.length,
    links: [],
  };
}

function wrapTravelDocuments(documents, packageId) {
  return {
    type: 'FeatureCollection',
    features: documents.map((doc) => ({
      type: 'Feature',
      id: doc.id,
      properties: {
        type: doc.type,
        package: doc.package,
        leg: doc.leg,
        travelDocumentType: doc.travelDocumentType,
        validity: doc.validity,
      },
      links: doc.link ? [doc.link] : [],
    })),
    properties: { type: 'travelDocuments' },
    numberMatched: documents.length,
    numberReturned: documents.length,
    links: [{ rel: 'self', href: `/collections/travel-documents/items?packageId=${packageId}` }],
  };
}

function wrapPayments(paymentList, filters) {
  return {
    type: 'FeatureCollection',
    features: paymentList.map((payment) => ({
      type: 'Feature',
      id: payment.id,
      properties: {
        amount: payment.amount,
        currencyCode: payment.currencyCode,
        category: payment.category,
        state: payment.state,
      },
      links: [],
    })),
    properties: { type: 'paymentCollection', ...filters },
    numberMatched: paymentList.length,
    numberReturned: paymentList.length,
    links: [],
  };
}

module.exports = {
  applyStandardHeaders,
  wrapPackage,
  wrapOfferCollection,
  wrapTravelDocuments,
  wrapPayments,
};
