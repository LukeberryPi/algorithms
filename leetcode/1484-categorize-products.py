# https://leetcode.com/problems/group-sold-products-by-the-date/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

activities_data = {
    'sell_date': ['2020-05-30', '2020-06-01', '2020-06-02', '2020-05-30', '2020-06-01', '2020-06-02', '2020-05-30'],
    'product': ['Headphone', 'Pencil', 'Mask', 'Basketball', 'Bible', 'Mask', 'T-Shirt']
}

activities_df = pd.DataFrame(activities_data)
activities_df['sell_date'] = pd.to_datetime(activities_df['sell_date'])

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities = activities.groupby('sell_date').agg(
        num_sold=('product', 'nunique'),
        products=('product', lambda x: ','.join(sorted(set(x))))
    ).reset_index()

    activities.sort_values('sell_date', inplace=True)

    return activities

print(categorize_products(activities_df))