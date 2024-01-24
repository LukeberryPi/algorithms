// https://www.codewars.com/kata/52fba66badcd10859f00097e/train/javascript

const sampleInput = "This website is for losers LOL!";

// receber uma string
// retornar essa string sem nenhuma vogal

function disemvowel(str) {
  const vowels = 'aeiouAEIOU';
  const split = str.split('');

  const disemvowelled = split.filter(char => !vowels.includes(char)).join('');

  return disemvowelled;
}

console.log(disemvowel(sampleInput));

