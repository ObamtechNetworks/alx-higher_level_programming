#!/usr/bin/node
// a script that calculates the factorial of a number
const arg = process.argv.slice(2)[0];

function factorial (n) {
  if (n === 0 || n === 1 || isNaN(n)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const number = parseInt(arg);
console.log(factorial(number));
