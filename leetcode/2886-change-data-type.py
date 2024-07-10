# https://leetcode.com/problems/change-data-type/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

def change_data_type(df):
    # grade was originally float64 and becomes int
    df["grade"] = df["grade"].astype(int)

    return df