// https://leetcode.com/problems/pascals-triangle/description/

function generate(n) {
  let ar = Array(n);

  if (n < 2) {
    return ar.fill();
  }

  // [1, 1] parent => [1, 2, 1] child
  for (let i = 1; ar.length <= n; i++) {
    if (ar[i - 1].length < 2) {
      ar[i] = [1, 1];
    }
  }

  return ar;
}

console.log(generate(2));
