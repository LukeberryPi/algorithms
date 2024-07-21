# https://leetcode.com/problems/students-and-examinations/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

students_data = {
    'student_id': [1, 2, 13, 6],
    'student_name': ['Alice', 'Bob', 'John', 'Alex']
}
students_df = pd.DataFrame(students_data)

subjects_data = {
    'subject_name': ['Math', 'Physics', 'Programming']
}
subjects_df = pd.DataFrame(subjects_data)

examinations_data = {
    'student_id': [1, 1, 1, 2, 1, 1, 13, 13, 13, 2, 1],
    'subject_name': ['Math', 'Physics', 'Programming', 'Programming', 'Physics', 'Math', 'Math', 'Programming', 'Physics', 'Math', 'Math']
}
examinations_df = pd.DataFrame(examinations_data)

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    result_df = students.merge(subjects, how="cross")

    count_df = examinations.value_counts().reset_index(name="count")

    return result_df.merge(count_df, how="left").fillna({'count': 0}).sort_values(by=['student_id', 'subject_name']).rename(columns={"count": "attended_exams"})

print(students_and_examinations(students_df, subjects_df, examinations_df))