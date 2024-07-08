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

if (squareSize < 0) {
  exit(0);
}

for (let i = 0; i < squareSize; i++) {
	console.log('X'.repeat(squareSize))
}
