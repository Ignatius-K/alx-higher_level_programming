#!/usr/bin/node
/*
 * 6-multi_languages
 * Written by Ignatius K <ignatiuskisekka@gmail.com>
 *
 * Script that logs using provided occurrences
 */
const { argv, exit } = require('node:process');
let number;
if (isNaN((number = argv[2]))) {
  console.log('Missing number of occurrences');
  exit(0);
}
for (let i = 0; i < number; i++) {
  console.log('C is fun');
}
