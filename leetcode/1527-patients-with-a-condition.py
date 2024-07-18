# https://leetcode.com/problems/patients-with-a-condition/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:

    def has_diabetes(condition: str) -> bool:
        return condition.startswith("DIAB1")

    return patients.loc[patients["conditions"].apply(has_diabetes)]