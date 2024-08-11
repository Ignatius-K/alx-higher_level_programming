/**
 * 9-script.js
 * Written by Ignatius K <ignatiuskisekka@gmail.com>
 *
 * Script that fetches a translation
 * displays value in <DIV#hello>
 *
 * Requirements:
 *  - JQuery
 */

/* eslint-disable no-undef */
$(document).ready(
  function () {
    const targetElement = $('DIV#hello');

    if (targetElement?.length > 0) {
      $.ajax({
        method: 'GET',
        url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
        dataType: 'json'
      }).done((data) => {
        if (data?.hello) {
          targetElement.text(data.hello);
        }
      });
    }
  }
);
/* eslint-disable no-undef */
