# https://leetcode.com/problems/create-a-new-column/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

def calculate_special_bonus(employees):
    employees["bonus"] = employees.apply(lambda row: row["salary"] if not row["name"].startswith("M") and row["employee_id"] % 2 != 0 else 0, axis=1)
    return employees.sort_values("employee_id")[["employee_id",  "bonus"]]