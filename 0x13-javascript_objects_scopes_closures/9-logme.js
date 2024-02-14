#!/usr/bin/node
// a function that prints the number of arguments already printed and the new arguent value

let count = 0;
exports.logMe = function (item) {
  return console.log(count++ + ': ' + item);
};
