#!/usr/bin/node
// A script that creates a class that defines a rectangle
// It has a constructor that takes two arguments w and h
// It initializes every instance's attributes with the value of the constructors parameter 'w' and 'h' for width and height respectively

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
