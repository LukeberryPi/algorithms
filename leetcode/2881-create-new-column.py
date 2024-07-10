# https://leetcode.com/problems/create-a-new-column/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

def create_new_column(df):
    df["bonus"] = df["salary"] * 2

    return df