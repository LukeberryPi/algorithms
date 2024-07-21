# https://leetcode.com/problems/classes-more-than-5-students/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

courses_data = {
    'student': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'class': ['Math', 'English', 'Math', 'Biology', 'Math', 'Math', 'Math']
}

courses_df = pd.DataFrame(courses_data)

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    courses = courses.groupby("class").filter(lambda x: len(x) >= 5)

    return courses[["class"]].drop_duplicates()

print(find_classes(courses_df))