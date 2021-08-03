#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const letter = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(letter.repeat(this.width));
    }
  }

  rotate () {
    const burbuja = this.width;
    this.width = this.height;
    this.height = burbuja;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
