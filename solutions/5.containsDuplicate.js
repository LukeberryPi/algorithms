const inputNums = [1, 2, 3, 4];

// return true if the list contains a duplicate
// false if it doesn't

function lazyContainsDuplicate(nums) {
  return nums.length !== new Set(nums).size;
}

function containsDuplicate(nums) {
  const map = new Map();
  let result = false;

  nums.forEach((num) => {
    if (!map.has(num)) {
      map.set(num, true);
    } else {
      result = true
    }
  })

  return result;
}

console.log(lazyContainsDuplicate(inputNums));
console.log(containsDuplicate(inputNums));
