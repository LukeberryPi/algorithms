# https://leetcode.com/problems/display-the-first-three-rows/submissions/1316418983/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

some_dataframe = None

def select_first_rows(employees):
    return employees.head(3)

print(select_first_rows(some_dataframe))