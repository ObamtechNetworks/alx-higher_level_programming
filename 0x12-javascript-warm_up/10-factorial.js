#!/usr/bin/node
const arg = process.argv.slice(2);

function factorial (n) {
  if (n === 0 || n === 1 || Number.isNaN(n)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const number = parseInt(arg[0]);
console.log(factorial(number));
