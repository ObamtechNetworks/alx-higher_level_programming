#!/usr/bin/node
const arg = process.argv.slice(2);

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

const first = arg[0];
const second = arg[1];

console.log(add(first, second));
