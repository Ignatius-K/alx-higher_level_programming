/**
 * 0-script.js
 * Written by Ignatius K <ignatiuskisekka@gmail.com>
 *
 * Script updates the text color of <header> element to `red`
 */

const targetElement = document.querySelector('header');
if (targetElement) {
  targetElement.style.setProperty('color', '#FF0000');
}
