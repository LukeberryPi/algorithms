# https://leetcode.com/problems/fill-missing-data/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

def fill_missing_values(df):
    df["A"] = df["A"].fillna(0)

    return df