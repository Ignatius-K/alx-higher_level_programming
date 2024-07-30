#!/usr/bin/node
/**
 * 1-writeme.js
 * Written by Ignatius K <ignatiuskisekka@gmail.com>
 *
 * Script that writes string to file
 *
 * Requirements:
 *  - @file: 1st argument (file to write to)
 *  - @string: 2nd argument (string to write)
 */

const fs = require('node:fs');
const { argv, exit } = require('node:process');

const NUMBER_OF_EXPECTED_ARGS = 4;
if (argv.length < NUMBER_OF_EXPECTED_ARGS) {
  exit(1);
}

fs.writeFile(
  argv[2],
  argv[3],
  { encoding: 'utf-8' },
  (error) => {
    if (error) {
      console.log(error);
      exit(1);
    }
  });
