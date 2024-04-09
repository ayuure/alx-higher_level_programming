#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let c = '';
      for (let j = 0; j < this.width; j++) {
        c += 'X';
      }
      console.log(c);
    }
  }

  rotate () {
    let t;
    t = this.height;
    this.height = this.width;
    this.width = t;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}

module.exports = Rectangle;
