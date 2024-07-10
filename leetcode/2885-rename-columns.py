# https://leetcode.com/problems/rename-columns/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

def rename_columns(df):
  df = df.rename(columns={"old_name": "new_name"})

  return df