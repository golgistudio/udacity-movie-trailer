#!/usr/bin/env node

require('babel-register');

const exec = require('child_process').exec;
const userHome = require('user-home');

/* eslint-disable no-console */
const initializeEvents = (processName) => {
  processName.stdout.on('data', (data) => {
    console.log(`stdout: ${data.toString()}`);
  });

  processName.stderr.on('data', (data) => {
    console.log(`stderr:  ${data.toString()}`);
  });

  processName.on('exit', (code) => {
    console.log(`child process exited with code: ${code.toString()}`);
  });
};
/* eslint-enable no-console */

const main = () => {
  /* eslint-disable max-len */
  const chromeDriverPath = `-Dwebdriver.chrome.driver="${userHome}/.selenium-binaries/chromedriver/2.22/chromedriver"`;
  const seleniumPath = `-jar ${userHome}/.selenium-binaries/selenium/2.53.1/selenium-server-standalone-2.53.1.jar`;

  const seleniumCommand = `java ${chromeDriverPath} ${seleniumPath}`;

  const seleniumProcess = exec(seleniumCommand);

  initializeEvents(seleniumProcess);
};

main();
