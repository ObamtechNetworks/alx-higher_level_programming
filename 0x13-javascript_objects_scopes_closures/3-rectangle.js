#!/usr/bin/node
// a script that creates a Rectangle class and then have a print method
// which prints the rectangle shape

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // Empty block
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
}

module.exports = Rectangle;
