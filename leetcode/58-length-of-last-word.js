// https://leetcode.com/problems/length-of-last-word/

const s = "    hello      world s  dssssssssss      ";

function lengthOfLastWord(s) {
  let curr = "";

  for (let i = s.length - 1; i >= 0; i--) {
    if (!curr && s[i] === " ") {
      continue;
    }

    if (curr && s[i] === " ") {
      break;
    }

    curr += s[i];
  }

  return curr.length;
}

console.log(lengthOfLastWord(s));
