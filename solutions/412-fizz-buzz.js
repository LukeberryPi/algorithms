// https://leetcode.com/problems/fizz-buzz/

const input = 15;

  function fizzBuzz(n) {
    let result = [];

    for (let i = 1; i <= n; i++) {
      if (i % 5 === 0 && i % 3 === 0) {
        result.push("FizzBuzz");
      } else if (i % 5 === 0) {
        result.push("Buzz");
      } else if (i % 3 === 0) {
        result.push("Fizz");
      } else {
        result.push(String(i));
      }
    }

    return result;
  }

console.log(fizzBuzz(input));
