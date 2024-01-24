// https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/javascript

const sampleInput = 'abracadabra';

function getCount(str) {
  const vowels = 'aeiou';
  let vowelsCount = 0;

  for (let letter of str) {
    if (vowels.includes(letter)) vowelsCount++
  }

  return vowelsCount
}

console.log(getCount(sampleInput));