#!/usr/bin/node

exports.esrever = function (list) {
// get the middle value ==> 4 [1, 2, 3, 4, 5]
// loop from beginning to middle: 2, 3,
// swap last element with first element: length - 1 - i = >
// length = 2, -1  => 1, - i ==> i = 0 ==> 1,
// length == 2, - 1, - i (2) ==> 1 -  1

  // another method
  // [1, 2, 3, 4]
  // set pointer to the first element -> first = arr[i]
  // length = arr.length
  // set pointer to the last eleemnt => last = arr[length - 1]
  // create a temp variable for swapping --> let temp
  // loop through the array and beging swapping
  // set last to temp ==> temp = last
  // set last to first --> last = first
  // set first to temp --> first = temp

  let start = 0;
  let end = list.length - 1;

  while (start < end) {
    const temp = list[start];
    list[start] = list[end];
    list[end] = temp;

    // move pointers towards each other
    start++;
    end--;
  }
  return list;
};
/**
const length = list.length;
const middle = Math.floor(length / 2); // get the integer val from lowest

// do swapping
let i = 0;
while (i < middle) {
  const temp = list[i];
  list[i] = list[length - 1 - i];
  list[length - 1 - i] = temp;
  i++;
}

return list;
**/
