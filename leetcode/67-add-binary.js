// https://leetcode.com/problems/add-binary/

const a = "11";
const b = "1";

// lazy implementation that passes most tests
// fails with weird input such as 
// let a = "10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101";
// let b = "110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011";
function addBinary(a, b) {
  const toInt = (bin) => {
    return parseInt(bin, 2);
  };

  const sum = toInt(a) + toInt(b);
  const toBin = (num) => {
    return (num >>> 0).toString(2);
  };
  return toBin(sum);
}

console.log(addBinary(a, b));

// https://chat.openai.com/share/e2b1517f-c2e6-44fa-aece-66b3f631c69f
// chatgpt implementation that passes all tests
function addBinary(a, b) {
  let result = "";
  let carry = 0;

  let maxLength = Math.max(a.length, b.length);

  for (let i = 0; i < maxLength || carry > 0; i++) {
    let digitA = i < a.length ? parseInt(a[a.length - 1 - i]) : 0;
    let digitB = i < b.length ? parseInt(b[b.length - 1 - i]) : 0;

    let sum = digitA + digitB + carry;
    carry = Math.floor(sum / 2);

    result = (sum % 2) + result;
  }

  return result;
}


let sum = addBinary(a, b);
console.log(sum);
