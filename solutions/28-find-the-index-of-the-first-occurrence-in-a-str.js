// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description

function findFirstOccurence(haystack, needle) {
  const result = haystack.match(needle);

  if (!result) return -1;

  return result.index;
}

console.log(findFirstOccurence("abcdefghijkdef", "def"));
