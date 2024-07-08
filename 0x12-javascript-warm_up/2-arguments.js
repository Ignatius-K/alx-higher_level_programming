#!/usr/bin/node
/*
 * 1-multi_languages
 * Written by Ignatius K <ignatiuskisekka@gmail.com>
 *
 * Script that target number of args
 */
const { argv } = require('node:process');
if (argv.length === 2) {
  console.log('No argument');
} else if (argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
