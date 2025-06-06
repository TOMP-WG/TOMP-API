# Migration help

To facilitate the migration (and creating wrappers), we provide a mapping toolbox between version 2.0 and 1.6 using jsonata.

## jsonata

Source: https://www.npmjs.com/package/jsonata

Reference implementation of the [JSONata query and transformation language](http://jsonata.org/).

* [JSONata in 5 minutes](https://www.youtube.com/embed/ZBaK40rtIBM)
* [JSONata language documentation](http://docs.jsonata.org/)
* [Try it out!](http://try.jsonata.org/)

## Installation

- `npm install jsonata`
- `npm install express jsonata body-parser yamljs`
- `npm install @apidevtools/swagger-parser`
- `npm install openapi-sampler`
- `npm install axios`

## Quick start

In Node.js:

```javascript
const jsonata = require('jsonata');

const data = {
    example: [
        {value: 4},
        {value: 7},
        {value: 13}
    ]
};

(async () => {
    const expression = jsonata('$sum(example.value)');
    const result = await expression.evaluate(data);  // returns 24
})()
```

## More information

* JSONata [documentation](http://docs.jsonata.org/)
* [JavaScript API](http://docs.jsonata.org/embedding-extending)
* [Intro talk](https://www.youtube.com/watch?v=TDWf6R8aqDo) at London Node User Group