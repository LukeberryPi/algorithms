# https://leetcode.com/problems/select-data/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

def select_data(some_df):
    return some_df.loc[some_df["student_id"] == 101, ["Name", "Age"]]