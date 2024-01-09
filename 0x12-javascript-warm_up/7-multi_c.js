#!/usr/bin/node
const arg = process.argv.slice(2);

const string = 'C is fun';
let i = 0;

const toInt = parseInt(arg[0]);
if (!isNaN(toInt)) {
  while (i < toInt) {
    console.log(string);
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
