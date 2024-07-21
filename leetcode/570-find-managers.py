# https://leetcode.com/problems/managers-with-at-least-5-direct-reports/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import numpy as np
import pandas as pd

data = {
    'id': [101, 102, 103, 104, 105, 106],
    'name': ['John', 'Dan', 'James', 'Amy', 'Anne', 'Ron'],
    'department': ['A', 'A', 'A', 'A', 'A', 'B'],
    'managerId': [np.nan, 101, 101, 101, 101, 101]
}

employee_df = pd.DataFrame(data)

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:

    # pandas way
    id_count = employee["managerId"].value_counts()
    employee["count"] = employee["id"].map(id_count).fillna(0).astype(int)

    # my proposition
    # def get_id_count(df, col):
    #   return df[col].value_counts()

    # employee["count"].map(get_id_count(employee, "managerId")).fillna(0).astype(int)

    return employee.loc[employee["count"] >= 5][["name"]]

print(find_managers(employee_df))