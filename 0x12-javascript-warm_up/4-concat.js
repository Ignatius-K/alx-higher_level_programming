#!/usr/bin/node
/*
 * 3-value_argument
 * Written by Ignatius K <ignatiuskisekka@gmail.com>
 *
 * Script that reads provided args
 */
const { argv } = require('node:process');
console.log(`${argv[2]} is ${argv[3]}`);
