# https://leetcode.com/problems/nth-highest-salary/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

data = pd.DataFrame({
    "employee_id": [1, 2, 3, 4, 5],
    "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "salary": [1000, 2000, 1500, 3000, 2000]
})

df = pd.DataFrame(data)

def nth_highest_salary(employee: pd.DataFrame, N: int):
    new_col = f"getNthHighestSalary({N})"

    if N > len(employee.drop_duplicates("salary").index):
        return pd.DataFrame({ new_col: [None] }) # should be None, leetcode is gapped

    # reset_index is used to remove index conflicts
    result_salary = employee.sort_values("salary", ascending=False).reset_index(drop=True).at[N - 1, "salary"]

    return pd.DataFrame({ new_col: [result_salary] })


print(nth_highest_salary(df, 2))

def gpt_nth_highest_salary(employee: pd.DataFrame, N: int):
    new_col = f"getNthHighestSalary({N})"

    distinct_salaries = employee["salary"].drop_duplicates().sort_values(ascending=False)

    if N > len(distinct_salaries):
        return pd.DataFrame({ new_col: [None] })

    sorted_salaries = distinct_salaries.reset_index(drop=True)
    nth_highest = sorted_salaries[N - 1]

    return pd.DataFrame({ new_col: [nth_highest] })


print(gpt_nth_highest_salary(df, 2))