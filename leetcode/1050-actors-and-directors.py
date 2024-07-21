# https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

actordirector_data = {
    'actor_id': [1, 1, 1, 1, 1, 2, 2],
    'director_id': [1, 1, 1, 2, 2, 1, 1],
    'timestamp': [0, 1, 2, 3, 4, 5, 6]
}

actordirector_df = pd.DataFrame(actordirector_data)

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    actor_director = actor_director.groupby(['actor_id', 'director_id']).agg(count=('timestamp', 'nunique')).reset_index()

    return actor_director.loc[actor_director["count"] >= 3][["actor_id", "director_id"]]

print(actors_and_directors(actordirector_df))