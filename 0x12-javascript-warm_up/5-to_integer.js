#!/usr/bin/node
const phrase = 'My number: ';
const number = process.argv[2];
if (!parseInt(number)) {
  console.log('Not a number');
} else {
  console.log(phrase + number);
}
