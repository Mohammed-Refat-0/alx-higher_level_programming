#!/usr/bin/node
if (process.argv[2] === undefined || (process.argv[2]) === null) {
  console.log('Missing number of occurrences');
} else {
  const x = Number(process.argv[2]);
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
