// migrates a TOMP-API 1.6 response to a TOMP-API v2.0 response
const jsonata = require('jsonata');
const fs = require('fs');

const args = process.argv.slice(2);

const map = {
    "planning-offers": "search-offers"
}

const data = require('./migrate v2/responses/' + args[0] + "-response.json")
const scriptContent = fs.readFileSync('./migrate v2/response-jsonata/' + args[0] + '-response.jsonata', 'utf8');

(async () => {
    const expression = jsonata(scriptContent);
    const result = await expression.evaluate(data);
    console.log("call /processes/" + map[args[0]] + "/execute with body: ");
    console.log(JSON.stringify(result, null, 2));
})()