# https://leetcode.com/problems/drop-duplicate-rows/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

# retains only the first occurence of the email.
# any other rows that come after and have the same email will be dropped
def drop_duplicate_emails(df):
    df = df.drop_duplicates(subset="email")

    return df