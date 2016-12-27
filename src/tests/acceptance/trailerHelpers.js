/* jslint-disable no-undef */
/* jslint-disable camelcase */
/* jslint-disable no-unused-vars */
const Helper = codecept_helper;

const async = require('async');
const chai = require('chai');

class TrailerHelpers extends Helper {
  // jslint-disable-next-line no-useless-constructor
  constructor(config) {
    super(config);
  }

  // before/after hooks
  _before() {
    this.browser = this.helpers.WebDriverIO.browser;
  }

  clickMovieCard(movieTitle) {
    return new Promise((resolve, reject) => {
      this.browser.elements('.movie-card')
      .then((elements) => {
        let match = -1;
        async.each(elements.value, (item, callback) => {
          this.browser.elementIdElement(item.ELEMENT, '.movie-description-header')
          .then((result) => {
            this.browser.elementIdText(result.value.ELEMENT)
            .then((cellElement) => {
              if (cellElement.value === movieTitle) {
                match = result.value.ELEMENT;
              }
              return callback();
            });
          });
        },
        (error) => {
          this.browser.elementIdClick(match);
          resolve();
        });
      });
    });
  }
}

module.exports = TrailerHelpers;
