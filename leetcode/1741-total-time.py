# https://leetcode.com/problems/find-total-time-spent-by-each-employee/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

employees_data = {
    'emp_id': [1, 1, 1, 2, 2],
    'event_day': ['2020-11-28', '2020-11-28', '2020-12-03', '2020-11-28', '2020-12-09'],
    'in_time': [4, 55, 1, 3, 47],
    'out_time': [32, 200, 42, 33, 74]
}

employees_df = pd.DataFrame(employees_data)

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees["total_time"] = employees["out_time"] - employees["in_time"]
    employees = employees.groupby(["emp_id", "event_day"])['total_time'].sum().reset_index()
    employees = employees.rename(columns={ "event_day": "day"})

    employees = employees[["day", "emp_id", "total_time"]]

    return employees.sort_values("day")

print(total_time(employees_df))