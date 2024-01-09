#!/usr/bin/node
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
