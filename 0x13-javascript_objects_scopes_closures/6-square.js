#!/usr/bin/node
const OldSquare = require('./5-square');

class Square extends OldSquare {
  constructor (size) {
    super(size);
    this.size = size;
  }

  double () {
    super.double();
    this.size *= 2;
  }

  charPrint (c) {
    if (c === undefined || c === null) { // check for falsy fvalues
      c = 'X';
    }

    for (let i = 0; i < this.size; i++) {
      let row = '';
      for (let j = 0; j < this.size; j++) {
        row += c;
      }
      console.log(row);
    }
  }
}
module.exports = Square;
