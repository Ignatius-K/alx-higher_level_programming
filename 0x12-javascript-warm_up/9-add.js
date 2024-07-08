#!/usr/bin/node
/*
 * 9-add
 * Written by Ignatius K <ignatiuskisekka@gmail.com>
 *
 * Script defines `add` for addition arithmetic
 */

const { argv } = require('node:process');

function add (param1, param2) {
  return (param1 + param2);
}

console.log(add(parseInt(argv[2]), parseInt(argv[3])));
