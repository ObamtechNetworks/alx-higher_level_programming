#!/usr/bin/node
// script that prints the addition of two numbers
const arg = process.argv.slice(2);

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

const first_num = arg[0];
const second_num = arg[1];

console.log(add(first_num, second_num));
