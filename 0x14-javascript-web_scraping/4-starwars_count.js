#!/usr/bin/node
/**
 * 4-starwars_count.js
 * Written by Ignatius K <ignatiuskisekka@gmail.com>
 *
 * Script that prints number of movies where character is present
 *
 * Requirements:
 *  - @url: 1st argument (URL to request)
 */

const request = require('request');
const { argv, exit } = require('node:process');

const NUM_OF_EXPECTED_ARGS = 3;
const CHARACTER_ID = 18;

if (argv.length < NUM_OF_EXPECTED_ARGS) {
  console.error(`Usage: node ${argv[1]} {URL_to_query}`);
  exit(1);
}

const url = argv[2];
request(url, {}, (error, response, body) => {
  if (error) {
    console.error(error);
    exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`code: ${response.statusCode}`);
    return;
  }

  const movies = JSON.parse(body).results;
  let characterMovies = 0;
  const requiredCharacterUrl = `https://swapi-api.alx-tools.com/api/people/${CHARACTER_ID}/`;
  Array.from(movies).forEach((movie) => {
    if (Array.from(movie.characters).find((characterUrl) => characterUrl === requiredCharacterUrl)) {
      characterMovies += 1;
    }
  });
  console.log(characterMovies);
});
