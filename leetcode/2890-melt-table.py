# https://leetcode.com/problems/reshape-data-melt/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

import pandas as pd

df = pd.DataFrame({
    'date': ['2023-01-01', '2023-01-02'],
    'A': [100, 120],
    'B': [150, 180]
})

def melt_table(df):
    melted_df = df.melt(id_vars=['date'], var_name='product', value_name='sales')

    return melted_df

print("input", df)
print("output", melt_table(df))
