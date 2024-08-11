/**
 * 3-script.js
 * Written by Ignatius K <ignatiuskisekka@gmail.com>
 *
 * Script that adds class `red` to <header>
 * When user clicks on the <div#red_header>
 *
 * Requirements:
 *  - JQuery
 */

/* eslint-disable no-undef */
const header = $('header');
const triggerElement = $('div#red_header');
if (triggerElement && header) {
  triggerElement.on('click', function () {
    header.addClass('red');
  });
}
/* eslint-enable no-undef */
