#!/usr/bin/node
/*
 * 101-call_me_moby
 * Written by Ignatius K
 *
 * Module that defines a function, executing another `x` times
 */
const { exit } = require('node:process');

exports.callMeMoby = function (x, functionToCall) {
  if (x < 0) exit(0);
  Array(x).fill().forEach(() => functionToCall.call());
};
