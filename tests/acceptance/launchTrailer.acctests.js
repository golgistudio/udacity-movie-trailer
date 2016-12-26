/* jshint-disable new-cap */
// jshint-disable-next-line no-undef
Feature('Moview Trailer Page');

// jshint-disable-next-line no-undef
Scenario('Launch trailer', (I) => {
  I.amOnPage('/');
  I.see('Hacksaw Ridge');
});
