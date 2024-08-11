/**
 * 2-script.js
 * Written by Ignatius K <ignatiuskisekka@gmail.com>
 *
 * Script that updates text color of <header> to `red`
 * when user clicks on <div#red_header>
 *
 * Requirements:
 *  - JQuery
 */

/* eslint-disable no-undef */
const targetElement = $('header');
if (targetElement) {
  $('div#red_header').on('click', () => {
    targetElement.css('color', 'red');
  });
}
/* eslint-enable no-undef */
