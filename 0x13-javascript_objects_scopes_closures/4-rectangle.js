#!/usr/bin/node

// create a Rectangle class in JavaScript
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // Empty block return an empty class
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = ''; // an empty string
      for (let j = 0; j < this.width; j++) {
        row += 'X';
        // process.stdout.write('X');
      }
      console.log(row);
      // process.stdout.write('\n');
    }
  }

  rotate () {
    // use a temp variable for the swapping or rotation
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () { // doubles the value of the width and height when method is called
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
