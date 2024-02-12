#!/usr/bin/node
// a script that searches for the second biggest integer in the list

const arg = process.argv.slice(2);

if (arg.length === 0 || arg.length === 1) {
  console.log(0);
} else {
  // convert string values to numbers
  const numbers = arg.map(Number);
  let largest = Number.MIN_SAFE_INTEGER; // Initialize largest to smallest possible integer;
  let secondLargest = Number.MIN_SAFE_INTEGER; // Initialize secondLargest to smallest possible integer

  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] > largest) {
      secondLargest = largest; // set second largest to be prev val of largest
      largest = numbers[i]; // set largest to the current big num
    } else if (numbers[i] > secondLargest && numbers[i] !== largest) {
      secondLargest = numbers[i];
    }
  }

  console.log(secondLargest); // print the second largest
}

/**
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
**/
