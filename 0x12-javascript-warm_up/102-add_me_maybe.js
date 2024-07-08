#!/usr/bin/node
/*
 * 102-add_me_maybe
 * Written by Ignatius K
 *
 * Script override a function arg by adding 1
 */

exports.addMeMaybe = function (number, functionToCall) {
  functionToCall(number + 1);
};
