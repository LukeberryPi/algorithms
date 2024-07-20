# https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

teacher_data = {
    'teacher_id': [1, 1, 1, 2, 2, 2, 2],
    'subject_id': [2, 2, 3, 1, 2, 3, 4],
    'dept_id': [3, 4, 3, 1, 1, 1, 1]
}

teacher_df = pd.DataFrame(teacher_data)

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    unique_subject_counts = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()
    unique_subject_counts.rename(columns={'subject_id': 'cnt'}, inplace=True)

    return unique_subject_counts

print(count_unique_subjects(teacher_df))