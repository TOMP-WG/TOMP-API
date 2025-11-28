const express = require('express');
const bodyParser = require('body-parser');
const jsonata = require('jsonata');
const fs = require('fs');
const path = require('path');
const SwaggerParser = require('@apidevtools/swagger-parser');
const endpointMap = require(path.join(__dirname, 'migrate v2/endpoint-mapping.json'));
const axios = require('axios');

const app = express();
const port = 3000;
const requestsDir = path.join(__dirname, 'migrate v2/request');
const responsesDir = path.join(__dirname, 'migrate v2/response');
const openApiV2 = path.join(__dirname, '../TOMP-API.yaml')

async function postV16(url, body) {
  console.log(`calling http://localhost:3001${url}`);
  try {
    const response = await axios.post('http://localhost:3001' + url, body);
    return response
  } catch (error) {
    console.error('Fout:', error.message);
  }
}

function addPost(baseRoutePath, methods) {
    if (methods.post && methods.post.operationId) {
        toAdd = {}
        operation = methods.post.operationId;
        if (baseRoutePath.includes('{')) {
            methods.post.parameters.forEach((p, i) => {
                if (p.in === 'path' && p.schema?.enum){
                    p.schema.enum.forEach( (enumValue, i2) => {
                        o2 = operation + '-' + enumValue;
                        r2 = baseRoutePath.replace('{' + p.name + '}', enumValue );
                        toAdd[o2] = r2;
                    });
                }
            });
        }
        else {
            toAdd[operation] = baseRoutePath;
        }

        Object.entries(toAdd).forEach( ([operationId, routePath]) => {
            const requestPath = path.join(requestsDir, `${operationId}.jsonata`);
            const responsePath = path.join(responsesDir, `${operationId}.jsonata`);

            if( !fs.existsSync(requestPath) )
                return;

            app.post(routePath, (req, res) => {
                const data = req.body;

                fs.readFile(requestPath, 'utf8', (err, expressionText) => {
                    if (err) {
                        return res.status(500).json({ error: `Kan expressie niet lezen voor '${operationId}': ${err.message}` });
                    }

                    try {
                        (async() => { 
                            const expression = jsonata(expressionText);
                            body = await expression.evaluate(data);
                            
                            url = endpointMap[operationId];

                            if (url.includes("{") ) {
                                const match = url.match(/{([^}]+)}/);
                                if (match) {
                                    toFind = match[1];
                                }
                                id = data.inputs[toFind];
                                url = url.replace(/{(\w+)}/g, id);
                            }

                            url = url.replace('POST ', '').replace('GET ', '');

                            result = await postV16(url, body)
                                .then( a => 
                                    {
                                        v16result = a.data;
                                        fs.readFile(responsePath, 'utf8', (err, responseJsonata) => {
                                            (async() => {
                                                const responseExpression = jsonata(responseJsonata);
                                                result = await responseExpression.evaluate(v16result);
                                                res.json(result);
                                            })()}
                                        ) 
                                    } );
                        })()
                    } catch (e) {
                        res.status(400).json({ error: `Fout in JSONata expressie: ${e.message}` });
                    }
                });
            });
            msg = `Endpoint geladen: POST ${routePath} => request/${operationId}.jsonata`;

            if (operationId in endpointMap) {
                msg += ' | ' + endpointMap[operationId] + ` | response/${operationId}.jsonata`
            }
            
            console.log(msg);
        } );
    }
}

function addGet(routePath, methods) {
    if (methods.get && methods.get.operationId) {
        const operationId = methods.get.operationId;
        const requestPath = path.join(requestsDir, `${operationId}.jsonata`);

        msg = `Endpoint geladen: GET ${routePath} => ${operationId}.jsonata`
        if (operationId == 'openApi') {
            msg = `Endpoint geladen: GET ${routePath} => TOMP-API.yaml`
        }

        if(operationId != 'openApi' && !fs.existsSync(requestPath))
            return;

        app.get(routePath, (req, res) => {
            const data = req.query;

            if (operationId == 'openApi' ){
                fs.readFile(openApi, (err, content) => { 
                    res.send(content); 
                } );
                return;
            }

            fs.readFile(requestPath, 'utf8', (err, expressionText) => {
                if (err) {
                    return res.status(500).json({ error: `Kan expressie niet lezen voor '${operationId}': ${err.message}` });
                }

                try {
                    (async() => { 
                        const expression = jsonata(expressionText);
                        const result = await expression.evaluate(data);
                        res.json(result);
                    })()                    
                } catch (e) {
                    res.status(400).json({ error: `Fout in JSONata expressie: ${e.message}` });
                }
            });
        });

        console.log(msg);
    }
}

app.use(bodyParser.json());

// Laad en parse de OpenAPI specificatie
if( !fs.existsSync(openApiV2) )
    return;

SwaggerParser.dereference(openApiV2)
  .then(api => {
    console.log('OpenAPI succesvol geladen en dereferenced.');
    setupServer(api); 
  })
  .catch(err => {
    console.error('Fout bij parsen/dereferencing van OpenAPI:', err.message);
    process.exit(1);
  });

function setupServer(openapi) {
    for (const [routePath, methods] of Object.entries(openapi.paths)) {
        routeV2 = '/v2' + routePath;
        addPost(routeV2, methods);
        addGet(routeV2, methods);
    }
}

app.listen(port, () => {
  console.log(`Server draait op http://localhost:${port}`);
});