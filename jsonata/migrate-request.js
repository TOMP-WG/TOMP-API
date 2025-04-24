// migrates a TOMP-API 2.0 request to a TOMP-API v1.6 request
const jsonata = require('jsonata');
const fs = require('fs');

const args = process.argv.slice(2);

const map = {
    "search-offers": "/plannings/offers",
    "purchase-product": "/bookings/onestop (assetType)",
    "use-asset": "/bookings/onestop (asset)"
}

const data = require('./migrate v2/requests/' + args[0] + "-request.json")
const scriptContent = fs.readFileSync('./migrate v2/request-jsonata/' + args[0] + '-request.jsonata', 'utf8');

(async () => {
    const expression = jsonata(scriptContent);
    const result = await expression.evaluate(data);
    console.log("call " + map[args[0]] + " with body: ");
    console.log(JSON.stringify(result, null, 2));
})()