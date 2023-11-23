// https://leetcode.com/problems/number-of-segments-in-a-string/

// const input = "Hello, my name is John";
const input = "Of all the gin joints in all the towns in all the world,   ";

function countSegments(str) {
  if (str.trim() === "") {
    return 0;
  }

  return str.split(" ").filter(Boolean).length;
}

console.log(countSegments(input));
