# https://leetcode.com/problems/daily-leads-and-partners/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

dailysales_data = {
    'date_id': ['2020-12-8', '2020-12-8', '2020-12-8', '2020-12-7', '2020-12-7',
                '2020-12-8', '2020-12-8', '2020-12-7', '2020-12-7', '2020-12-7'],
    'make_name': ['toyota', 'toyota', 'toyota', 'toyota', 'toyota',
                  'honda', 'honda', 'honda', 'honda', 'honda'],
    'lead_id': [0, 1, 1, 0, 0, 1, 2, 0, 1, 2],
    'partner_id': [1, 0, 2, 2, 1, 2, 1, 1, 2, 1]
}

dailysales_df = pd.DataFrame(dailysales_data)
dailysales_df["date_id"] = pd.to_datetime(dailysales_df["date_id"])

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
     daily_sales = daily_sales.groupby(['date_id', 'make_name']).agg(
        unique_leads=('lead_id', 'nunique'),
        unique_partners=('partner_id', 'nunique')
    ).reset_index()

     return daily_sales

print(daily_leads_and_partners(dailysales_df))