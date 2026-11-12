const jwt = require('jsonwebtoken');
const config = require('../config');

function issueToken(clientId) {
  const accessToken = jwt.sign({ clientId }, config.jwtSecret, { expiresIn: config.tokenTtlSeconds });
  return { accessToken, expiresIn: config.tokenTtlSeconds };
}

function verifyToken(token) {
  return jwt.verify(token, config.jwtSecret);
}

module.exports = { issueToken, verifyToken };
