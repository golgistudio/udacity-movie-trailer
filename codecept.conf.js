exports.config = {
  helpers: {
    WebDriverIO: {
      url: 'http://localhost:8000',
      browser: 'chrome'
    },
    FileSystem: {},
  },
  bootstrap: false,
  name: 'recording-admin',
  mocha: {},
  tests: './src/tests/acceptance/*.acctests.js',
  timeout: 10000,
  // windowSize does not seem to work yet.
  windowSize: '1024x1000',
  output: '.codecept.log',
  include: {
  }
};
