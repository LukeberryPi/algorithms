// https://www.hackerrank.com/challenges/arrays-ds/problem?isFullScreen=true

const sampleInput = [1, 2, 3, 4, 5];

function reverseArray(arr) {
  let reversedArray = [];

  for (let i = arr.length - 1; i >= 0; i--) {
    reversedArray.push(arr[i]);
  }

  return reversedArray;
}

console.log(reverseArray(sampleInput));
