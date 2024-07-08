#!/usr/bin/node
/*
 * 8-square
 * Written by Ignatius K <ignatiuskisekka@gmail.com>
 *
 * Script that print square
 */
const { argv, exit } = require('node:process');

let squareSize;
if (!(squareSize = parseInt(argv[2]))) {
  console.log('Missing size');
  exit(0);
}
Array(squareSize).fill().forEach(() => {
  console.log('x'.repeat(squareSize));
});
