# https://leetcode.com/problems/drop-missing-data/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

def drop_none(df):
    df = df.dropna(subset="name")

    return df