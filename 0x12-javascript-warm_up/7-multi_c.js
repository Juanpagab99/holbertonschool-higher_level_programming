#!/usr/bin/node
const x = process.argv[2];
const phrase = 'C is fun';
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 1; i <= x; i++) {
    console.log(phrase);
  }
}
