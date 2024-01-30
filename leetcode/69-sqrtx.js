// https://leetcode.com/problems/sqrtx/description/

const x = 1085817232;

// lazy implementation that fails on leetcode because it is too slow
function sqrt(x) {
  if (x < 2) return x;
  const start = Math.floor(x / 2);
  for (let i = start; i >= 1; i--) {
    if (i * i <= x) return i;
  }
}

console.log(sqrt(x));

// cryptic algorithm implementation that works
// explanation: https://chat.openai.com/share/b4084630-9235-46f8-b6e1-b306239f4edf
function sqrtBabylonian(x, tolerance = 1e-10) {
  if (x < 0) return NaN; // Square root of a negative number is not a real number

  let guess = x / 2;
  let previousGuess;

  do {
    previousGuess = guess;
    guess = 0.5 * (guess + x / guess);
  } while (Math.abs(guess - previousGuess) > tolerance);

  return guess;
}

// Example usage:
let number = 1085817232;
let squareRoot = sqrtBabylonian(number);

console.log(`Square root of ${number} is approximately: ${squareRoot}`);
