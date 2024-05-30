// https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/description/

// const rectangles = [
//   [5, 8],
//   [3, 9],
//   [5, 12],
//   [16, 5],
// ];

const rectangles = [
  [2, 3],
  [3, 7],
  [4, 3],
  [3, 7],
];

function countGoodRectangles(rectangles) {
  const lengthOfLargestSquare = (arr) => {
    return Math.min(...arr);
  };

  let nOfLargest = 0;
  let largest = 0;

  for (let rect of rectangles) {
    if (lengthOfLargestSquare(rect) > largest) {
      largest = lengthOfLargestSquare(rect);
    }
  }

  for (let rect of rectangles) {
    if (lengthOfLargestSquare(rect) === largest) {
      nOfLargest++;
    }
  }

  return nOfLargest;
}

console.log(countGoodRectangles(rectangles));
