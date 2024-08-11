/**
 * 7-script.js
 * Written by Ignatius K <ignatiuskisekka@gmail.com>
 *
 * Script that fetches character name
 * and displays it in <DIV#character>
 *
 * Requirements:
 *  - JQuery
 */

/* eslint-disable no-undef */
const targetElement = $('DIV#character');

if (targetElement) {
  $.ajax({
    method: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    dataType: 'json'

  }).done((data) => {
    targetElement.text(data?.name);
  });
}
/* eslint-enable no-undef */
