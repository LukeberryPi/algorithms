# https://leetcode.com/problems/create-a-dataframe-from-list/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

import pandas as pd

st = [[1,15],[2,11],[3,11],[4,20]]

def create_dataframe_from_list(student_data):
    df = pd.DataFrame(student_data, columns=["student_id", "age"])

    return df

print(create_dataframe_from_list(st))