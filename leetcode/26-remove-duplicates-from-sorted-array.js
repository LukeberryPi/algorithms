// https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

let nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 6, 7, 7];
let nums1 = [1, 1, 2];

function removeDuplicates(nums) {
  const seen = new Map();

  for (let i = 0; i < nums.length; i++) {
    let count = nums.reduce((acc, cur) => {
      if (cur === nums[i]) {
        acc++;
      }

      return acc;
    }, 0);

    if (seen.has(nums[i])) {
      nums.splice(i, count - 1);
    }
    seen.set(nums[i], true);
  }

  return nums;
}

removeDuplicates(nums);
removeDuplicates(nums1);

console.log(nums);
console.log(nums1);
