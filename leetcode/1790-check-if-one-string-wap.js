// https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

// const s1 = "bank";
// const s2 = "knab";

const s1 = "bankb";
const s2 = "kannb";

function areAlmostEqual(s1, s2) {
  if (s1 === s2) {
    return true;
  }

  if (s1.length !== s2.length) {
    return false;
  }

  if (!s1.split("").every((ch) => s2.split("").includes(ch))) {
    return false;
  }

  if (!s2.split("").every((ch) => s1.split("").includes(ch))) {
    return false;
  }

  let differentChars = 0;

  for (let i = 0; i < s1.length; i++) {
    if (s1[i] !== s2[i]) {
      differentChars++;
    }
  }

  return differentChars === 2;
}

console.log(areAlmostEqual(s1, s2));
