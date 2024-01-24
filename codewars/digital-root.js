// https://www.codewars.com/kata/541c8630095125aba6000c00/train/javascript

const sampleInput = 942;

// somar todos os algarismos do número
// caso o número seja menor que 10, retorne o número
// caso não seja, some os algarismos do número produzido novamente

function digitalRoot(n) {
  if (n < 10) return n;

  const split = String(n).split('').map(e => parseInt(e));
  const sum = split.reduce((acc, cur) => acc + cur);

  return digitalRoot(sum);
}

console.log(digitalRoot(sampleInput));
