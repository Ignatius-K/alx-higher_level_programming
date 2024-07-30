#!/usr/bin/node
/**
 * 3-starwars_title.js
 * Written by Ignatius K <ignatiuskisekka@gmail.com>
 *
 * Script that prints title of Star wars movie
 *
 * Requirements:
 *  - @movieID: 1st argument
 */

const { argv, exit } = require('node:process');
const request = require('request');

const NUM_OF_EXPECTED_ARGS = 3;
if (argv.length < NUM_OF_EXPECTED_ARGS) {
  exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;
request(url, {}, (error, __, body) => {
  if (error) {
    console.log(error);
    exit(1);
  }
  console.log(JSON.parse(body).title);
});
