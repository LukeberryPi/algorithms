const ar = [1, 5, null, 7, 2, 9, null, 4];

let result = [];
let subArray = [];

for (let i = 0; i <= ar.length; i++) {
  const cur = ar[i];
  const isNumber = (x) => x === +x;

  if (isNumber(cur)) {
    subArray.push(cur);
  } else {
    result.push(subArray);
    subArray = [];
  }
}

console.log(reduced);
