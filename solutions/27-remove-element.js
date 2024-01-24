// https://leetcode.com/problems/remove-element/description/

let nums = [1, 2, 6, 6, 6, 6, 3, 4, 5, 6];
let val = 6;

// why iterate backwards? https://chat.openai.com/share/2a596495-d1d0-43bb-9cec-b55213db9a9b
function removeElement(nums, val) {
  for (let i = nums.length; i >= 0; i--) {
    if (nums[i] === val) {
      nums.splice(i, 1);
    }
  }

  return nums.length;
}

console.log('removeElement(nums, val)', removeElement(nums, val))
console.log('nums', nums)