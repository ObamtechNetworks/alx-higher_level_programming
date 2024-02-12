#!/usr/bin/node
// script that prints the addition of two numbers
const arg = process.argv.slice(2);

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

const firstNum = arg[0];
const secondNum = arg[1];

console.log(add(firstNum, secondNum));
