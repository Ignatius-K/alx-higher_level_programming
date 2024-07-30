#!/usr/bin/node
/**
 * 2-statuscode.js
 * Written by Ignatius K <ignatiuskisekka@gmail.com>
 *
 * Script that displays the status code of `GET` request
 *
 * Requirements:
 *   - @url: 1st argument (URL to request)
 *   - request: module to be used
 */

const request = require('request');
const { argv, exit } = require('node:process');

const NUM_OF_EXPECTED_ARGS = 3;
if (argv.length < NUM_OF_EXPECTED_ARGS) {
  exit(1);
}

request(argv[2], { method: 'GET' }, (error, response) => {
  if (error) {
    console.log(error);
    exit(1);
  }
  console.log(`code: ${response.statusCode}`);
});
