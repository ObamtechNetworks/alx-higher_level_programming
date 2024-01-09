#!/usr/bin/node
const arg = process.argv.slice(2);

let i = 0;
const str = 'x';

const toInt = parseInt(arg[0]);
if (!isNaN(toInt)) {
  while (i < toInt) {
    console.log(str.repeat(toInt));
    i++;
  }
} else {
  console.log('Missing size');
}
