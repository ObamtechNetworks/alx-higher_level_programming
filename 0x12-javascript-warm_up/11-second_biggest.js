#!/usr/bin/node
const arg = process.argv.slice(2);

if (arg.length === 0 || arg.length === 1) {
  console.log(0);
} else {
  // convert string valuest to number
  const numbers = arg.map(Number);
  const biggestIndex = numbers.indexOf(Math.max(...numbers));
  numbers.splice(biggestIndex, 1); // remove the biggest
  const secondLargest = Math.max(...numbers);
  console.log(secondLargest); // print the second largest
}
