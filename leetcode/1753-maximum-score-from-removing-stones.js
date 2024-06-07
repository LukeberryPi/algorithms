// https://leetcode.com/problems/maximum-score-from-removing-stones/

const maxScore = (a, b, c) => {
  let score = 0;
  let piles = [a, b, c];

  const select = (piles) => {
    piles.sort((a, b) => b - a);

    if (piles[0] !== 0 && piles[1] !== 0) {
      return [0, 1];
    }

    if (piles[0] !== 0 && piles[2] !== 0) {
      return [0, 2];
    }

    if (piles[1] !== 0 && piles[2] !== 0) {
      return [1, 2];
    }
  };

  const remove = (indexAr) => {
    piles[indexAr[0]]--;
    piles[indexAr[1]]--;
  };

  while (true) {
    let selected = select(piles);
    if (!selected) {
      return score;
    }
    remove(selected);
    score++;
  }
};

console.log(maxScore(2, 4, 6));
