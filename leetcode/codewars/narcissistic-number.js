// https://www.codewars.com/kata/5287e858c6b5a9678200083c/train/javascript

const sampleInput = 153;

// número narcisista é um número em que a soma de todos
// os seus dígitos individualmente elevados ao comprimento
// do número é igual ao próprio número
// recebemos um número e devemos retornar uma bool true or false

// 7 => 7^1 => 7 => true (é narcisista)
// 21 => 2^2 + 1^2 => 5 => false (não é narcisista)
// 371 => 3^3 + 7^3 + 1^3 => 371 => true (é narcisista)

function narcissistic(n) {
  const length = n.toString().length;
  const digits = n.toString().split('').map(digit => parseInt(digit))

  let sumOfPoweredDigits = 0;

  digits.forEach(digit => {
    sumOfPoweredDigits += digit ** length
  })

  return n === sumOfPoweredDigits;
}

console.log(narcissistic(sampleInput));