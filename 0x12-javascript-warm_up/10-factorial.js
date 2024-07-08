#!/usr/bin/node
/*
 * 10-factorial
 * Written by Ignatius K <ignatiuskisekka@gmail.com>
 *
 * Script that computes factorial of an arg
 */

const { argv } = require('node:process');

function factorial (number) {
  if (isNaN(number)) {
    return 1;
  }
  if (number === 0) {
    return 1;
  }
  return number * factorial(number - 1);
}

console.log(factorial(parseInt(argv[2])));
