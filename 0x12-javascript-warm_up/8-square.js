#!/usr/bin/node
const arg = process.argv.slice(2)[0];

let i = 0;
const str = 'X';

const toInt = parseInt(arg);
if (!isNaN(toInt)) {
  while (i < toInt) {
    console.log(str.repeat(toInt));
    i++;
  }
} else {
  console.log('Missing size');
}
