/**
 * 5-script.js
 * Written by Ignatius K <ignatiuskisekka@gmail.com>
 *
 * Script that adds a <li> to <ul.my_list>
 *
 * Requirements:
 *  - JQuery
 */

/* eslint-disable no-undef */
const listOfElements = $('UL.my_list');
const triggerElement = $('DIV#add_item');

if (listOfElements && triggerElement) {
  const elementToAdd = '<li>Item</li>';
  triggerElement.on('click', function () {
    listOfElements.append(elementToAdd);
  });
}
/* eslint-enable no-undef */
