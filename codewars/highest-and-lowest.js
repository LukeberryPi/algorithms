// https://www.codewars.com/kata/554b4ac871d6813a03000035/train/javascript

const sampleInput = "8 3 -5 42 -1 0 0 -9 4 7 4 -4";

function highAndLow(numbers) {
  const array = numbers.split(' ');

  return `${Math.max(...array)} ${Math.min(...array)}`;
}

console.log(highAndLow(sampleInput));