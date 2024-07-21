# https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

data_people = {
    'id': [1, 7, 11, 90, 3],
    'name': ['Alice', 'Bob', 'Meir', 'Winston', 'Jonathan']
}

people_df = pd.DataFrame(data_people)

data_employee_uni = {
    'id': [3, 11, 90],
    'unique_id': [1, 2, 3]
}

employee_uni_df = pd.DataFrame(data_employee_uni)

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    return employees.merge(employee_uni, on="id", how="left")[["unique_id", "name"]]

print(replace_employee_id(people_df, employee_uni_df))