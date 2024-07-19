# https://leetcode.com/problems/rank-scores/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

scores_data = {
    'id': [1, 2, 3, 4, 5, 6],
    'score': [3.50, 3.65, 4.00, 3.85, 4.00, 3.65]
}
scores_df = pd.DataFrame(scores_data)

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores.sort_values("score", ascending=False, inplace=True)
    scores["rank"] = scores["score"].rank(method="dense", ascending=False).astype(int)

    return scores[["score", "rank"]]


print(order_scores(scores_df))