/* jshint-disable new-cap */
// jshint-disable-next-line no-undef
Feature('Moview Trailer Page');

// jshint-disable-next-line no-undef
Scenario('Launch trailer', function * scen(I) {
  I.amOnPage('/');
  I.waitForText('War Dogs');
  I.see('War Dogs');
  I.clickMovieCard('War Dogs');
  I.waitForElement({css: '#trailer'});
  I.seeElement({css: '#trailer'});
  I.wait(3);
  I.saveScreenshot('trailer.png');
  I.seeInSource('<iframe id="trailer-video" type="text-html" src="https://www.youtube.com/embed/Rwh9c_E3dJk?autoplay=1&amp;html5=1" frameborder="0"></iframe>');
});
