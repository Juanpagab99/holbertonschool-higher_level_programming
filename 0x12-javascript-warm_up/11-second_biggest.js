#!/usr/bin/node
const number = process.argv.splice(2);
const len = number.length;
if (len < 2) {
  console.log('0');
} else {
  number.sort((x, y) => x - y);
  console.log(number[len - 2]);
}
