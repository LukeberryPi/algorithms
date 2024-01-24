// https://www.hackerrank.com/challenges/kangaroo/problem?isFullScreen=true

const sampleInput = {
  aKangarooInitialPosition: 0,
  aKangarooSpeed: 3,
  bKangarooInitialPosition: 4,
  bKangarooSpeed: 2,
};

const {
  aKangarooInitialPosition,
  aKangarooSpeed,
  bKangarooInitialPosition,
  bKangarooSpeed,
} = sampleInput;

function kangaroo(x1, v1, x2, v2) {
  if (v2 > v1) return "NO";
  
  return ((x2 - x1) % (v1 - v2) === 0 && "YES") || "NO";
}

console.log(
  kangaroo(
    aKangarooInitialPosition,
    aKangarooSpeed,
    bKangarooInitialPosition,
    bKangarooSpeed
  )
);
