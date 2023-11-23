// https://leetcode.com/problems/convert-a-number-to-hexadecimal/

const input = 5;

const dict = {
  10: "a",
  11: "b",
  12: "c",
  13: "d",
  14: "e",
  15: "f",
}

function toHex(n) {
  return n % 16;
}

console.log(toHex(input))