// https://leetcode.com/problems/plus-one/description/

const digits = [6, 1, 4, 5, 3, 9, 0, 1, 9, 5, 1, 8, 6, 7, 0, 5, 5, 4, 3];
// const digits = [1, 2, 3];
// const digits = [9];
// const digits = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9];

function plusOne(digits) {
  return (BigInt(digits.join("").toString()) + BigInt(1))
    .toString()
    .split("")
    .map((x) => +x);
}

console.log(plusOne(digits));
