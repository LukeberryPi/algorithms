// https://www.codewars.com/kata/550f22f4d758534c1100025a/javascript

const sampleInput = "The quick brown fox jumps over the lazy dog.";

function isPangram(string) {
  let lettersOnly = string.replace(/[^a-zA-Z]/g, "").toLowerCase();
  let lettersArray = lettersOnly.split("");
  const uniqueLetters = Array.from(new Set(lettersArray));

  return uniqueLetters.length === 26 ? true : false;
}

console.log(isPangram(sampleInput));
