// const inputNums = [1, 2, 3, 1];
// const inputK = 3;
// const inputNums = [1, 2, 3, 1, 2, 3];
// const inputK = 2;
const inputNums = [0, 1, 2, 3, 4, 0, 0, 7, 8, 9, 10, 11, 12, 0];
const inputK = 1;

// Given an integer array nums and an integer k
// return true if there are two distinct indices i and j in the array
// such that nums[i] == nums[j] and abs(i - j) <= k.

// .every() / .some() instead of .forEach() for a circuit break gimmick:
// https://stackoverflow.com/questions/6260756/how-to-stop-javascript-foreach
function containsDuplicateTwo(nums, k) {
  const map = new Map();
  let result = false;

  nums.some((num, idx) => {
    if (!map.has(num)) {
      map.set(num, idx);
    } else {
      const absoluteDifference = Math.abs(map.get(num) - idx);
      result = absoluteDifference <= k;
      if (result === true) {
        return true;
      }
      map.set(num, idx);
    }
  });

  return result;
}

console.log(containsDuplicateTwo(inputNums, inputK));
