const { Router } = require('express');
const config = require('../config');
const { resolveProvider } = require('../data/providers');

const router = Router();
const activeProvider = resolveProvider(config.provider);

router.get('/health', (req, res) => {
  res.status(200).json({
    status: 'ok',
    time: new Date().toISOString(),
    // Which operator this instance simulates - handy when running several sandboxes at once
    // (different PORT + SANDBOX_PROVIDER) to tell them apart. See README.md.
    provider: { key: activeProvider.key, name: activeProvider.name, mode: activeProvider.mode },
  });
});

module.exports = router;
