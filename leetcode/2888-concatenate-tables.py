# https://leetcode.com/problems/reshape-data-concatenate/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

import pandas as pd

def concatenate_tables(df1, df2):
    final_df = pd.concat([df1, df2])

    return final_df