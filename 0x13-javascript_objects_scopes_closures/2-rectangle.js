#!/usr/bin/node
// create a Rectangle class, constructor must take two arg: w and h
// if w or h === 0 or not a +ve integer, create an emtpy object
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // Empty block
    }
  }
}

module.exports = Rectangle;
