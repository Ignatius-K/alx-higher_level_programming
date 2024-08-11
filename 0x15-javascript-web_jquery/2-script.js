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

// const targetElement = document.querySelector('header')
// const triggerElement = document.querySelector('div#red_header')
// if (triggerElement) {
//   triggerElement.addEventListener('click', () => {
//     targetElement.style.setProperty('color', '#FF0000')
//   })
// }
