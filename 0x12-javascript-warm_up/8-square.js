#!/usr/bin/node
const number = process.argv[2];
const letter = 'X';
if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    console.log(letter.repeat(number));
  }
}
