// https://leetcode.com/problems/longest-common-prefix/

const strs = ["flower", "flow", "flight"];

function longestCommonPrefix(arr) {
  const smallest = arr.sort((a, b) => a.length - b.length)[0];

  return smallest;
}

console.log(longestCommonPrefix(strs));
