// https://leetcode.com/problems/reverse-words-in-a-string/description/

const input = "the sky is blue";

function reverseWords(s) {
  return s.trim().split(" ").reverse().join(" ");
}

console.log(reverseWords(input));
