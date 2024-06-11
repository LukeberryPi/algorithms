// create a multiply function that receives two ints and returns the result
// of multiplication between them. you cannot use *.

function multiply(a, b) {
  if (a == 0 || b == 0) {
    return 0;
  }

  return a / (1 / b);
}

// bugs when b is negative
function multiplyWhile(a, b) {
  if (a == 0 || b == 0) {
    return 0;
  }

  let result = 0;

  while (b !== 0) {
    result += a;
    b > 0 ? b-- : b++; 33
  }

  return result;
}

// also bugs when b is negative
function multTwitter(a, b) {
  let c = 0;

  while (a !== 0) {
    c += b;
    if (a < 0) {
      a = a + 1;
    } else {
      a = a - 1;
    }
  }

  return c;
}

console.log("multiply(2, 3)", multiply(2, 3));
console.log("multiply(4, 9)", multiply(4, 9));
console.log("multiply(-2, 10)", multiply(-2, 10));
console.log("multiply(10, -2)", multiply(10, -2));

console.log("multiplyWhile(2, 3)", multiplyWhile(2, 3));
console.log("multiplyWhile(4, 9)", multiplyWhile(4, 9));
console.log("multiplyWhile(-2, 10)", multiplyWhile(-2, 10));
console.log("multiplyWhile(10, -2)", multiplyWhile(10, -2));

console.log("multTwitter(2, 3)", multTwitter(2, 3));
console.log("multTwitter(4, 9)", multTwitter(4, 9));
console.log("multTwitter(-2, 10)", multTwitter(-2, 10));
console.log("multTwitter(10, -2)", multTwitter(10, -2));
