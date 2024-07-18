# https://leetcode.com/problems/article-views-i/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return views.loc[views["author_id"] == views["viewer_id"], ["viewer_id"]].rename(columns={"viewer_id": "id"}).sort_values("id").drop_duplicates("id")