# https://leetcode.com/problems/second-highest-salary/submissions/1325480973/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

data = pd.DataFrame({
    "employee_id": [1, 2, 3, 4],
    "salary": [1000, 1500, 3000, 3000]
})

df = pd.DataFrame(data)

def second_highest_salary(employee: pd.DataFrame):
    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)

    if len(unique_salaries) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})

    second_highest = unique_salaries.iloc[1]

    return pd.DataFrame({'SecondHighestSalary': [second_highest]})


print(second_highest_salary(df))