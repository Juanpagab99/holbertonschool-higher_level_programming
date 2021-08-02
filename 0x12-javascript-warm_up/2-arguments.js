#!/usr/bin/node
const tam = process.argv.length;
if (tam < 3) {
	console.log('No argument');
} else if (tam === 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
