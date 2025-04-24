const jsonata = require('jsonata');
const fs = require('fs');

const args = process.argv.slice(2);
const data = require('./migrate v2/1.6/' + args[0] + "-request.json")
const scriptContent = fs.readFileSync('./migrate v2/1.6/search-offers-request.jsonata', 'utf8');

(async () => {
    const expression = jsonata(scriptContent);
    const result = await expression.evaluate(data);
    console.log(JSON.stringify(result, null, 2));
})()