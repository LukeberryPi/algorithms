# https://leetcode.com/problems/find-users-with-valid-e-mails/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

data = {
    "user_id": [1, 2, 3, 4, 5, 6, 7],
    "name": ["Winston", "Jonathan", "Annabelle", "Sally", "Marwan", "David", "Shapiro"],
    "mail": ["winston@leetcode.com", "jonathanisgreat", "bella-@leetcode.com", "sally.come@leetcode.com", "quarz#2020@leetcode.com", "david69@gmail.com", ".shapo@leetcode.com"]
}

df = pd.DataFrame(data)

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    valid_symbols = ["_", "-", "."]

    def is_valid_email(email):
        prefix = email.split('@')[0]
        return prefix[0].isalpha() and all(char.isalnum() or char in valid_symbols for char in prefix)

    return users.loc[
        (users["mail"].apply(is_valid_email)) &
        (users["mail"].str.endswith("@leetcode.com"))
    ]

print(valid_emails(df)) 
