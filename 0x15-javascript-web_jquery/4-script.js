/**
 * 4-script.js
 * Written by Ignatius K <ignatiuskisekka@gmail.com>
 *
 * Script that toggles class of <header>
 * when user clicks <div#toggle_header>
 *
 * Requirements:
 *  - JQuery
 */

/* eslint-disable no-undef */
const header = $('header');
const triggerElement = $('DIV#toggle_header');
const classNames = ['red', 'green'];

if (header && triggerElement) {
  triggerElement.on('click', function () {
    classNames.forEach(className => header.toggleClass(className));
  });
}
/* eslint-enable no-undef */
