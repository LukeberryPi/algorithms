// https://www.hackerrank.com/challenges/the-birthday-bar/problem?isFullScreen=true

const sampleInput = {
  numbersOnChocolate: [2, 2, 1, 3, 2],
  birthDay: 4,
  birthMonth: 2,
};

const { numbersOnChocolate, birthDay, birthMonth } = sampleInput;

function birthday(s, d, m) {
  const candidateSegments = s
    .reduce((acc, _, i, arr) => {
      acc.push(arr.slice(i, i + m));

      return acc;
    }, [])
    .filter((seg) => seg.length === m);

  const correctSegments = candidateSegments.filter(
    (seg) => seg.reduce((acc, cur) => acc + cur) === d
  );

  return correctSegments.length;
}

console.log(birthday(numbersOnChocolate, birthDay, birthMonth));
