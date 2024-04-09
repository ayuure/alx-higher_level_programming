#!/usr/bin/node
const SquareE = require('./5-square');

class Square extends SquareE {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let si = '';
      for (let j = 0; j < this.width; j++) {
        si += c;
      }
      console.log(si);
    }
  }
}

module.exports = Square;
