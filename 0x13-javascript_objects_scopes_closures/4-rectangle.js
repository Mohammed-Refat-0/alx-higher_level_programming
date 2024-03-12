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

  rotate () {
    const x = this.width;
    this.width = this.height;
    this.height = x;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
