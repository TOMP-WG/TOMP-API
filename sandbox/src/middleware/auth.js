const { verifyToken } = require('../lib/jwt');
const { TompError } = require('../lib/errors');

module.exports = function auth(req, res, next) {
  const header = req.headers.authorization;
  if (!header || !header.startsWith('Bearer ')) {
    return next(new TompError({ errorcode: 4, type: 'AUTH', status: 401, title: 'Missing bearer token' }));
  }
  const token = header.slice('Bearer '.length).trim();
  try {
    req.auth = verifyToken(token);
    return next();
  } catch (err) {
    return next(new TompError({ errorcode: 4, type: 'AUTH', status: 401, title: 'Invalid or expired token', detail: err.message }));
  }
};
