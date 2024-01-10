#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let i = 0;
    while (i < this.size) {
      let j = 0;
      let row = '';
      i++;
      while (j < this.size) {
        row += c;
        j++;
      }
      console.log(row);
    }
  }
}
module.exports = Square;
