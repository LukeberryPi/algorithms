# https://leetcode.com/problems/delete-duplicate-emails/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

df = pd.DataFrame({
    "name": ["luke", "victor", "henry"],
    "email": ["luke", "luke", "victor"]
})

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by='id', inplace=True)
    person.drop_duplicates(subset='email', inplace=True)
    person.reset_index(drop=True, inplace=True)

print(delete_duplicate_emails(df))