#!/usr/bin/node
const arg = process.argv.slice(2)[0]; // collect cmd arg directly

const string = 'C is fun';
let i = 0;
const toInt = parseInt(arg);

if (!isNaN(toInt)) {
  while (i < toInt) {
    console.log(string);
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
