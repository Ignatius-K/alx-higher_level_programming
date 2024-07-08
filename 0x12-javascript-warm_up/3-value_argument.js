#!/usr/bin/node
/*
 * 3-value_argument
 * Written by Ignatius K <ignatiuskisekka@gmail.com>
 *
 * Script that prints first arg
 */
const { argv, exit } = require('node:process');
if (argv.length === 2) {
  console.log('No argument');
  exit(0);
}
console.log(argv[2]);
