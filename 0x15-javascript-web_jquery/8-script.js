/**
 * 8-script.js
 * Written by Ignatius K <ignatiuskisekka@gmail.com>
 *
 * Script that fetches and lists the title for all movies
 * lists them in the <UL#list_movies>
 *
 * Requirements:
 *  - JQuery
 */

/* eslint-disable no-undef */
const movieList = $('UL#list_movies');
const another = $('div#fgsfgfs');
console.log(movieList);
console.log(another);

if (movieList) {
  $.ajax({
    method: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    dataType: 'json'

  }).done((data) => {
    const tempList = $('<ul/>');

    data?.results.forEach((movie) => {
      const tempLi = $('<li/>').text(movie?.title ? movie?.title : 'No title');
      tempList.append(tempLi);
    });
    movieList.html(tempList.html());
  });
}
/* eslint-disable no-undef */
