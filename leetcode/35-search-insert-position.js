// https://leetcode.com/problems/search-insert-position/description

const nums = [
  1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
];
const target = 8;

function binarySearch(nums, target) {
  const len = nums.length;
  const mid = nums[Math.floor(len / 2)];

  while (mid !== target) {}

  return mid;
}

console.log("binarySearch(nums, target)", binarySearch(nums, target));
