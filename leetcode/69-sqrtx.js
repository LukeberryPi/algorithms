// https://leetcode.com/problems/sqrtx/description/

const x = 4;

function sqrt(x) {
  const start = Math.floor(x / 2);
  for (let i = start; i >= 2; i--) {
    if (i * i <= x) return i;
  }
  return undefined;
}

console.log(sqrt(x));
