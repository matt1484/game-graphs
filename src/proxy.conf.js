var process = require("process");
module.exports = [{
  context: [
    "/api/**"
  ],
  target: process.env.PROXY_URL || 'http://localhost:8000',
  secure: false
}];