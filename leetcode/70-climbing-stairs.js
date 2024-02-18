// https://leetcode.com/problems/climbing-stairs/

// 1 => 1 step => 1 possibility
// 2 => 1 + 1 / 2 => 2 p
// 3 => 1 + 1 + 1 / 1 + 2 / 2 + 1 => 3 p
// 4 => 1 + 1 + 1 + 1 / 2 + 1 + 1 / 1 + 2 + 1 / 1 + 1 + 2 / 2 + 2 => 5 p
// 5 => 1 + 1 + 1 + 1 + 1 / 2 + 1 + 1 + 1 / 1 + 2 + 1 + 1 / 1 + 1 + 2 + 1 / 1 + 1 + 1 + 2 / 2 + 2 + 1 / 2 + 1 + 2 / 1 + 2 + 2 => 8

// sum of the two previous possibilities
// fibonacci type beat
// for a new step, you can reach it either by:
//    taking one step from the previous step
//    taking two steps from the second to last step 

function climbingStairs(n) {
  if (n <= 2) {
    return n;
  }

  let ar = new Array(n + 1);
  ar[1] = 1;
  ar[2] = 2;

  for (let i = 3; i <= n; i++) {
    ar[i] = ar[i - 1] + ar[i - 2];
  }

  return ar[n];
}

console.log(climbingStairs(5));
