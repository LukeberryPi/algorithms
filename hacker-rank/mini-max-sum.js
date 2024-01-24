// https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true

const sampleInput = [1, 2, 3, 4, 5];

function miniMaxSum(arr) {
  const totalArrSum = arr.reduce((acc, cur) => acc + cur);

  let miniSum = totalArrSum - Math.max(...arr);
  let maxSum = totalArrSum - Math.min(...arr);

  return [miniSum, maxSum];
}

console.log(miniMaxSum(sampleInput));
