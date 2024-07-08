#!/usr/bin/node
/*
 * 101-call_me_moby
 * Written by Ignatius K
 *
 * Module that defines a function, executing another `x` times
 */

exports.callMeMoby = function (x, functionToCall) {
  Array(x).fill().forEach(() => functionToCall.call());
};
