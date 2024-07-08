#!/usr/bin/node
/*
 * 11-second_biggest
 * Written by Ignatius K <ignatiuskisekka@gmail.com>
 *
 * Script that logs the second biggest argument
 */

const { argv, exit } = require('node:process');

if (argv.length <= 3) {
  console.log(0);
  exit(0);
}

const args = argv.slice(2).map((arg) => parseInt(arg))
  .sort((a, b) => b - a);
console.log(args[1]);
