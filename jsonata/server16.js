const express = require('express');
const SwaggerParser = require('@apidevtools/swagger-parser');
const OpenAPISampler = require('openapi-sampler');
const path = require('path');

const app = express();
const port = 3001;

// Laad en dereference de OpenAPI spec
const openapiPath = path.join(__dirname, 'TOMP-API-1.6.yaml');

SwaggerParser.dereference(openapiPath)
  .then(openapi => {
    console.log('✅ OpenAPI geladen.');

    for (const [route, methods] of Object.entries(openapi.paths)) {
      for (const [method, operation] of Object.entries(methods)) {
        if (method != 'parameters') {
            const responses = operation.responses || {};
            const statusCode = Object.keys(responses).find(code => responses[code].content);
            const content = statusCode ? responses[statusCode].content['application/json'] : null;

            // Zoek naar example of examples
            let example = null;
            if (content?.example) {
              example = content.example;
            } else if (content?.examples) {
              const first = Object.values(content.examples)[0];
              example = first.value || null;
            } else if (content?.schema?.example) {
              example = content.schema.example;
            } else if (content.schema) {
              try {
                example = OpenAPISampler.sample(content.schema, { skipReadOnly: true });
              } catch (e) {
                console.warn(`⚠️  Kan geen voorbeeld genereren voor ${method.toUpperCase()} ${route}: ${e.message}`);
                continue;
              }
            }

            if (!example) {
              console.warn(`⚠️  Geen voorbeeld gevonden voor ${method.toUpperCase()} ${route}`);
              continue;
            }

            const realRoute = route.replace(/{(\w+)}/g, ':$1');

            // Route aanmaken
            const handler = (req, res) => {
              console.log( realRoute + ' called')
              res.status(Number(statusCode) || 200).json(example);
            };

            switch (method.toLowerCase()) {
            case 'get':
                app.get( '/v1' + realRoute, handler);
                break;
            case 'post':
                app.post('/v1' + realRoute, handler);
                break;
            case 'put':
                app.put('/v1' + realRoute, handler);
                break;
            case 'delete':
                app.delete('/v1' + realRoute, handler);
                break;
            }

            console.log(`📡 Endpoint aangemaakt: [${method.toUpperCase()}] /v1${realRoute} → voorbeeld response (${statusCode})`);
        }
      }
    }

    app.listen(port, () => {
      console.log(`🚀 Mock API actief op http://localhost:${port}`);
    });
  })
  .catch(err => {
    console.error(`❌ Fout bij laden van OpenAPI: ${err.message}`);
  });
