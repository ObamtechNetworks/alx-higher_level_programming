#!/usr/bin/node

// make function visible to the outside
exports.add = function add (a, b) {
  return parseInt(a) + parseInt(b);
};
