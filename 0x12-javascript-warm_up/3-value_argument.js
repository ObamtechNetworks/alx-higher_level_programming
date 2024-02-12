#!/usr/bin/node
// script ath prints the first argument passed to it
const arg = process.argv.slice(2);

if (!arg[0]) {
  console.log('No argument');
} else {
  console.log(arg[0]);
}

/**
const arg = process.argv.slice(2);

let isEmpty = true;

arg.forEach((val, index) => {
  if (index === 0) {
    console.log(`${val}`);
  }
  isEmpty = false;
});

if (isEmpty) {
  console.log('No argument');
}
**/
