# https://leetcode.com/problems/get-the-size-of-a-dataframe/submissions/1316413219/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

import pandas as pd

some_dataframe = None

def get_size_of_dataframe(players):
    return [len(players.index), len(players.columns)]

print(get_size_of_dataframe(some_dataframe))