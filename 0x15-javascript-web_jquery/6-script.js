/**
 * 6-script.js
 * Written by Ignatius K <ignatiuskisekka@gmail.com>
 *
 * Script that updates the text of the <header> to `New Header!!!`
 * when user clicks on <DIV#update_header>
 *
 * Requirements:
 *  - JQuery
 */

/* eslint-disable no-undef */
const header = $('header');
const triggerElement = $('DIV#update_header');

if (header && triggerElement) {
  triggerElement.on('click', function () {
    header.html('New Header!!!');
  });
}
/* eslint-disable no-undef */
