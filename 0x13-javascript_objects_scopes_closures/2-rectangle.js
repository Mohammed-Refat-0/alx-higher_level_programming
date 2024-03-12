#!/usr/bin/node

// Defines a "Rectangle" class
class Rectangle {
  width;
  height;

  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
