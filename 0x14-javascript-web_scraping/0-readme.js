#!/usr/bin/node
/**
 * 0-readme.js
 * Written by Ignatius K <ignatiuskisekka@gmail.com>
 *
 * Script that reads and print the content of file
 *
 * Requirement:
 * - @file: 1st argument
 */

const fs = require('node:fs');
const { argv, exit } = require('node:process');

if (argv.length < 3) {
  exit(1);
}

fs.readFile(argv[2], { encoding: 'utf-8' }, (error, data) => {
  if (error) {
    console.log(error);
    exit(1);
  }
  console.log(data);
});
