#!/usr/bin/node
/**
 * 5-request_store.js
 * Written by Ignatius K <ignatiuskisekka@gmail.com>
 *
 * Script that gets content of webpage and stores it in file
 *
 * Requirements:
 *  - @url: 1st arg (URL to request)
 *  - @file_path: 2nd arg (file to store the response body)
 */

const { argv, exit } = require('node:process');
const fs = require('node:fs');
const request = require('request');

const NUM_OF_EXPECTED_ARGS = 4;
if (argv.length < NUM_OF_EXPECTED_ARGS) {
  console.error(`Usage: node ${argv[1]} {url} {file}`);
  exit(1);
}

const url = argv[2];
const filePath = argv[3];
request(url, {}, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`code: ${response.statusCode}`);
    return;
  }

  fs.writeFile(filePath, body, { encoding: 'utf-8' }, (error) => {
    if (error) {
      console.error(error);
    }
  });
});
