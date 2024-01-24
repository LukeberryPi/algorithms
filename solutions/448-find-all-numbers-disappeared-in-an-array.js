// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

const input = [4, 3, 2, 7, 8, 2, 3, 1];
// const input = [1, 1];

// Time O(n²) ; Space O(n)
function findDisappearedNumbersWithArray(nums) {
  const length = nums.length;
  const result = [];

  for (let i = 1; i <= length; i++) {
    if (!nums.includes(i)) {
      result.push(i);
    }
  }

  return result;
}

// Time O(n) ; Space O(n)
function findDisappearedNumbersWithSet(nums) {
  const set = new Set(nums);
  let result = [];

  for (let i = 1; i <= nums.length; i++) {
    if (!set.has(i)) {
      result.push(i);
    }
  }

  return result;
}

function benchmark(testName, callback) {
  const startTime = performance.now();
  callback();
  const endTime = performance.now();
  console.log(testName, `time: ${endTime - startTime}`);
}

// benchmark("withArray", () => findDisappearedNumbersWithArray(input));
// benchmark("withSet", () => findDisappearedNumbersWithSet(input));

// worth studying all solutions:
// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/solutions/1583736/c-python-all-6-solutions-w-explanations-binary-search-hashset-2x-o-1-space-approach/