# https://leetcode.com/problems/count-salary-categories/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

accounts_data = {
    'account_id': [3, 2, 8, 6],
    'income': [108939, 12747, 87709, 91796]
}
accounts_df = pd.DataFrame(accounts_data)

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    accounts["Low Salary"] = accounts["income"] < 20000
    accounts["Average Salary"] = (accounts["income"] >= 20000) & (accounts["income"] <= 50000)
    accounts["High Salary"] = accounts["income"] > 50000

    return pd.DataFrame({
        "category": ["Low Salary", "Average Salary", "High Salary"],
        "accounts_count": [accounts["Low Salary"].sum(), accounts["Average Salary"].sum(), accounts["High Salary"].sum()]
    })

print(count_salary_categories(accounts_df))
