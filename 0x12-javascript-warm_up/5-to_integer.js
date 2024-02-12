#!/usr/bin/node
// a script that attempts to convert arg pass to it if its a number and print a msg

const arg = process.argv.slice(2)[0]; // get the first cmd arg

const toInt = parseInt(arg); // convert the arg to number using Number constructor
console.log(!isNaN(toInt) ? `My number: ${toInt}` : 'Not a number');

/**
const arg = process.argv.slice(2);

const toInt = parseInt(arg[0]);
if (!isNaN(toInt)) {
  console.log(`My number: ${toInt}`);
} else {
  console.log('Not a number');
}
*/
