#!/usr/bin/node
/**
 * 100-starwars_characters.js
 * Written by Ignatius K <ignatiuskisekka@gmail.com>
 *
 * Script that prints characters of Star Wars movie
 */

const { argv, exit } = require('node:process');
const request = require('request');

const NUM_OF_EXPECTED_ARGS = 3;
if (argv.length < NUM_OF_EXPECTED_ARGS) {
  console.error(`Usage: ${argv[1]} {movie_id}`);
  exit(1);
}

const MOVIE_ID = argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${MOVIE_ID}/`;
request(url, {}, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.info(`Failed with code: ${response.statusCode}`);
    return;
  }

  const characters = JSON.parse(body).characters;
  characters.forEach(characterUrl => handleQueryCharacter(characterUrl));
});

/**
 * @param {string} characterUrl
 * @returns void
 */
const handleQueryCharacter = (characterUrl) => {
  if (!characterUrl) {
    return;
  }
  request(characterUrl, {}, (error, response, body) => {
    if (error) {
      return;
    }

    if (response.statusCode !== 200) {
      return;
    }

    console.log(JSON.parse(body).name);
  });
};
