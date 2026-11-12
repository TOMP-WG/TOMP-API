const fs = require('node:fs');

const createApp = require('./app');
const config = require('./config');

if (process.argv.includes('--reset')) {
  fs.rmSync(config.dataFile, { force: true });
  console.log(`--reset: removed ${config.dataFile}`);
}

createApp()
  .then((app) => {
    app.listen(config.port, () => {
      console.log(`TOMP-API sandbox listening on http://localhost:${config.port}`);
    });
  })
  .catch((err) => {
    console.error('Failed to start sandbox server', err);
    process.exit(1);
  });
