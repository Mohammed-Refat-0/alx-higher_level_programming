#!/usr/bin/node
// Defines a "square" class that inherits from class "Rectangle"

const Squarev = require('./5-square');

class Square extends Squarev {
  charPrint (c) {
    if (isNaN(this.char)) {
      c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
  }
}

module.exports = Square;
