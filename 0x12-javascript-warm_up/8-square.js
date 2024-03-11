#!/usr/bin/node
if (process.argv[2] === undefined || (process.argv[2]) === null) {
  console.log('Missing size');
} else {
  const x = Number(process.argv[2]);
  for (let i = 0; i < x; i++) {
    console.log('x'.repeat(x));
  }
}
