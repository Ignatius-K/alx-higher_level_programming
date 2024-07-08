#!/usr/bin/node
/*
 * 5-to_integer
 * Written by Ignatius K <ignatiuskisekka@gmail.com>
 *
 * Script that logs the number
 */
const { argv, exit } = require('node:process');
let number;
if ((number = parseInt(argv[2]))) {
  console.log(`My number: ${number}`);
  exit(0);
}
console.log('Not a number');
