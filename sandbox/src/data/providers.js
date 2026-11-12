// Example shared-mobility data for Amsterdam and Utrecht.
//
// In the real TOMP ecosystem, every operator (MSP) runs its own TOMP-API instance; a MaaS
// platform calls each one separately. This sandbox mirrors that: each running instance simulates
// exactly one operator, picked via SANDBOX_PROVIDER (see ../config.js and ../../.env.example).
// Start several instances with a different PORT + SANDBOX_PROVIDER to simulate several operators
// side by side - see "Simulating different providers" in sandbox/README.md.

const CITIES = {
  amsterdam: { name: 'Amsterdam', center: { lat: 52.3676, lon: 4.9041 }, radiusKm: 6 },
  utrecht: { name: 'Utrecht', center: { lat: 52.0907, lon: 5.1214 }, radiusKm: 5 },
};

// Each provider offers a single mode (as real operators do) with a handful of seed vehicles
// scattered across the cities it covers. Coordinates are approximate real-world locations, close
// enough for a believable demo - not meant to be precise.
const PROVIDERS = {
  gosharing: {
    key: 'gosharing',
    name: 'GoSharing',
    mode: 'BICYCLE',
    pricing: { basePrice: 1.0, perMinute: 0.19 },
    vehicles: [
      { id: 'gosharing-ams-01', city: 'amsterdam', lat: 52.3731, lon: 4.8922 }, // Jordaan
      { id: 'gosharing-ams-02', city: 'amsterdam', lat: 52.365, lon: 4.885 }, // De Pijp
      { id: 'gosharing-utr-01', city: 'utrecht', lat: 52.0904, lon: 5.1158 }, // Utrecht Centraal
      { id: 'gosharing-utr-02', city: 'utrecht', lat: 52.0865, lon: 5.128 }, // Utrecht Science Park
    ],
  },
  felyx: {
    key: 'felyx',
    name: 'Felyx',
    mode: 'MOPED',
    pricing: { basePrice: 0.89, perMinute: 0.21 },
    vehicles: [
      { id: 'felyx-ams-01', city: 'amsterdam', lat: 52.368, lon: 4.9036 }, // Centrum
      { id: 'felyx-ams-02', city: 'amsterdam', lat: 52.3545, lon: 4.8768 }, // Zuid
      { id: 'felyx-utr-01', city: 'utrecht', lat: 52.0924, lon: 5.1079 }, // Utrecht Centrum
    ],
  },
  check: {
    key: 'check',
    name: 'Check',
    mode: 'BICYCLE',
    pricing: { basePrice: 0.75, perMinute: 0.15 },
    vehicles: [
      { id: 'check-ams-01', city: 'amsterdam', lat: 52.36, lon: 4.8852 }, // Oud-West
      { id: 'check-ams-02', city: 'amsterdam', lat: 52.3785, lon: 4.9 }, // Centraal Station
    ],
  },
  uber: {
    key: 'uber',
    name: 'Uber',
    mode: 'TAXI',
    pricing: { basePrice: 4.5, perKm: 1.95 },
    vehicles: [
      { id: 'uber-ams-01', city: 'amsterdam', lat: 52.3791, lon: 4.9003 }, // Centraal Station
      { id: 'uber-ams-02', city: 'amsterdam', lat: 52.355, lon: 4.87 }, // Zuid/WTC
      { id: 'uber-utr-01', city: 'utrecht', lat: 52.0894, lon: 5.1077 }, // Utrecht Centrum
    ],
  },
  bolt: {
    key: 'bolt',
    name: 'Bolt',
    mode: 'TAXI',
    pricing: { basePrice: 3.9, perKm: 1.65 },
    vehicles: [
      { id: 'bolt-ams-01', city: 'amsterdam', lat: 52.368, lon: 4.912 },
      { id: 'bolt-ams-02', city: 'amsterdam', lat: 52.34, lon: 4.865 },
    ],
  },
  viavan: {
    key: 'viavan',
    name: 'ViaVan',
    mode: 'TAXI',
    pricing: { basePrice: 4.1, perKm: 1.55 },
    vehicles: [
      { id: 'viavan-utr-01', city: 'utrecht', lat: 52.0902, lon: 5.1147 },
      { id: 'viavan-utr-02', city: 'utrecht', lat: 52.101, lon: 5.073 }, // Utrecht Overvecht
    ],
  },
};

const DEFAULT_PROVIDER_KEY = 'gosharing';

function resolveProvider(key) {
  return PROVIDERS[key] || PROVIDERS[DEFAULT_PROVIDER_KEY];
}

function listProviderKeys() {
  return Object.keys(PROVIDERS);
}

function toRad(deg) {
  return (deg * Math.PI) / 180;
}

function haversineKm(a, b) {
  const earthRadiusKm = 6371;
  const dLat = toRad(b.lat - a.lat);
  const dLon = toRad(b.lon - a.lon);
  const sinLat = Math.sin(dLat / 2);
  const sinLon = Math.sin(dLon / 2);
  const h = sinLat * sinLat + Math.cos(toRad(a.lat)) * Math.cos(toRad(b.lat)) * sinLon * sinLon;
  return 2 * earthRadiusKm * Math.asin(Math.sqrt(h));
}

// Parses this codebase's `gps:<lat>,<lon>` place references (the only place format the sandbox's
// example data understands); returns null for anything else (postal codes, stop ids, ...).
function parseGps(place) {
  if (typeof place !== 'string') return null;
  const match = /^gps:(-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)$/.exec(place.trim());
  if (!match) return null;
  return { lat: Number(match[1]), lon: Number(match[2]) };
}

// Finds the provider's nearest vehicle to `place`, as long as it's within its city's coverage
// radius. Returns null when `place` isn't GPS, or this provider has nothing reachable there -
// e.g. a taxi-only provider has no BICYCLE offer, or a provider that only covers Amsterdam has
// nothing near Utrecht.
function findNearestVehicle(provider, place) {
  const point = parseGps(place);
  if (!point) return null;
  let best = null;
  for (const vehicle of provider.vehicles) {
    const city = CITIES[vehicle.city];
    const distanceKm = haversineKm(point, vehicle);
    if (distanceKm > city.radiusKm) continue;
    if (!best || distanceKm < best.distanceKm) best = { vehicle, city, distanceKm };
  }
  return best;
}

module.exports = {
  CITIES,
  PROVIDERS,
  DEFAULT_PROVIDER_KEY,
  resolveProvider,
  listProviderKeys,
  findNearestVehicle,
  parseGps,
};
