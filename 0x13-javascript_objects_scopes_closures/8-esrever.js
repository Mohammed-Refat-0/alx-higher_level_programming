#!/usr/bin/node
// Function that returns the reversed version of a list
exports.esrever = function (list) {
  const x = list.length;

  for (let i = 0; i < x / 2; i++) {
    const temp = list[i];
    list[i] = list[x - i - 1];
    list[x - i - 1] = temp;
  }
};
