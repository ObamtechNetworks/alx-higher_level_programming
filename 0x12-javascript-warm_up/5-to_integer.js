#!/usr/bin/node
const arg = process.argv.slice(2);

const toInt = parseInt(arg[0]);
if (!isNaN(toInt)) {
  console.log(`My number: ${toInt}`);
} else {
  console.log('Not a number');
}
