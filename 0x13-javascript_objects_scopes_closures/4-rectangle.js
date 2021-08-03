#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let letter = '';
    for (let i = 0; i < this.height; i++) {
      letter = 'X';
      for (let j = 0; j < this.width; j++) {
        letter = letter + 'X';
      }
      console.log(letter + '');
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
