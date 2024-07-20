# https://leetcode.com/problems/game-play-analysis-i/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

activity_data = {
    'player_id': [1, 1, 2, 3, 3],
    'device_id': [2, 2, 3, 1, 4],
    'event_date': ['2016-03-01', '2016-05-02', '2017-06-25', '2016-03-02', '2018-07-03'],
    'games_played': [5, 6, 1, 0, 5]
}

df = pd.DataFrame(activity_data)
df['event_date'] = pd.to_datetime(df['event_date'])

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity.sort_values("event_date", inplace=True)
    activity.drop_duplicates(subset="player_id", inplace=True)
    activity.rename(columns={"event_date": "first_login"}, inplace=True)

    return activity[["player_id", "first_login"]].sort_values("player_id")


print(game_analysis(df))