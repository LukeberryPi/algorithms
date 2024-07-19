# https://leetcode.com/problems/department-highest-salary/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

employee_data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['Joe', 'Jim', 'Henry', 'Sam', 'Max'],
    'salary': [70000, 90000, 80000, 60000, 90000],
    'departmentId': [1, 1, 2, 2, 1]
}
employee = pd.DataFrame(employee_data)

# Creating the department DataFrame
department_data = {
    'id': [1, 2],
    'name': ['IT', 'Sales']
}
department = pd.DataFrame(department_data)

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame):
    merged_df = employee.merge(department, left_on='departmentId', right_on='id', suffixes=('', '_dept'))
    merged_df.drop(columns='id_dept', inplace=True)

    merged_df["highest_salary"] = merged_df.groupby("departmentId")["salary"].transform('max')
    merged_df = merged_df.loc[merged_df["salary"] == merged_df["highest_salary"]]
    merged_df = merged_df.rename(columns={ "name": "Employee", "salary": "Salary", "name_dept": "Department"})[["Employee", "Salary", "Department"]]

    cols = merged_df.columns.tolist()
    cols.insert(0, cols.pop())

    return merged_df[cols]

print(department_highest_salary(employee, department))