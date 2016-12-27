exports.config = {
  helpers: {
    WebDriverIO: {
      url: 'http://localhost:8000',
      browser: 'chrome'
    },
    FileSystem: {},
    TrailerHelpers: {
      require: './src/tests/acceptance/trailerHelpers.js'
    }
  },
  bootstrap: false,
  name: 'movie-trailer',
  mocha: {},
  tests: './src/tests/acceptance/*.acctests.js',
  timeout: 10000,
  // windowSize does not seem to work yet.
  windowSize: '1024x1000',
  output: './src/tests/acceptance/screenshots',
  include: {
  }
};
