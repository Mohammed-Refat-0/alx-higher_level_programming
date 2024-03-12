#!/usr/bin/node

// Defines a "Rectangle" class
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const x = this.height;
    const y = this.width;
    for (let i = 0; i < x; i++) {
      console.log('X'.repeat(y));
    }
  }
}
module.exports = Rectangle;
