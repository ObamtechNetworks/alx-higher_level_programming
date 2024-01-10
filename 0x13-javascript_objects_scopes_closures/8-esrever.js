#!/usr/bin/node

exports.esrever = function (list) {
// get the middle value ==> 4
// loop from beginning to middle: 2, 3,
// swap last element with first element: length - 1 - i = >
// length = 2, -1  => 1, - i ==> i = 0 ==> 1,
// length == 2, - 1, - i (2) ==> 1 -  1

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
};
