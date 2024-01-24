// https://leetcode.com/problems/arranging-coins/

const input = 5;

function arrangeCoins(n) {
  let remaining = n;
  let rowsCompleted = 0;

  while (remaining > rowsCompleted) {
    rowsCompleted += 1
    remaining -= rowsCompleted;
  }

  return rowsCompleted;
}

console.log(arrangeCoins(input));