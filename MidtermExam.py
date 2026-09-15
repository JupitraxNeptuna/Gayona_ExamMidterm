import numpy as np
import pandas as pd

class InvalidScoreError(Exception):
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
        message = (
            f"In {self.name}'s Record: The score, {self.score} is outside the range (0-100)."
        )
        super().__init__(message)

class StudentRecordLockedError(Exception):
    def __init__(self, name):
        self.name = name
        message = (
            f"In {self.name}'s Record: You cannot add a score to a locked record."
        )
        super().__init__(message)

    raw_rows = [
        {"name": " Amara ", "scores": "92,85,78"},
        {"name": "Leo", "scores": "88,91,73"},
        {"name": "Priya", "scores": "65,72,150"},         
        {"name": "Sam", "scores": "70,not_a_number,60"},  
        {"name": "Amara", "scores": "95,90,88"},          
        {"name": "Jade", "scores": "81,77,84,90"},
    ]

df = pd.DataFrame(raw_rows)

print(df)
print(df.describe[])
df["name"] = df["name"].str.strip()
df["scores"] = df["scores"].str.strip()
df = df.drop_duplicates(subset=['name', keep='first'])


class Student:
    def __init__(self, name: str, scores):
        self.name = name.strip()
        self.is_locked = False

        self.scores = scores_array