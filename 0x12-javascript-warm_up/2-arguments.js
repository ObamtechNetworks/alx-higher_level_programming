#!/usr/bin/node
const arg = process.argv.slice(2);
// or can do: -> const { argv } = require('node:process'); destructuring

if (arg.length < 1) {
  console.log('No argument');
} else if (arg.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
