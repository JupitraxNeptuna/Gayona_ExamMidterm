import pandas as pd
import numppy as np

class InvalidScoreError(Exception):
    """Raised when a score is non-numeric, out of range (0-100), or empty."""
    pass

class StudentRecordLockedError(Exception):
    """Raised when attempting to modify a locked student record."""
    pass

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
print(df.describe())
df["name"] = df ["name"] .str.strip()
df["scores"] = df["scores"].str.strip().str.title() 

df["names"] = df["names"].fillna(df["names"].mean())
df = df.drop_duplicates()
print(df) 
print(df.describe()) 

class Student:
    def __init__(self, name: str, scores):
        self.name = name.strip()
        self._is_locked = False
        
        try:
            scores_array = np.array(scores, dtype=float)
        except (ValueError, TypeError) as e:
            raise InvalidScoreError(f"Scores for student '{self.name}' could not be converted to numbers: {e}")
        
        if scores_array.size == 0:
            raise InvalidScoreError(f"Student '{self.name}' must have at least one score.")
            
        if np.any(scores_array < 0) or np.any(scores_array > 100):
            invalid_vals = scores_array[(scores_array < 0) | (scores_array > 100)].tolist()
            raise InvalidScoreError(f"Student '{self.name}' has out-of-range scores (0-100 allowed): {invalid_vals}")
            
        self.scores = scores_array


if __name__ == "__main__":
    raw_rows = [
        {"name": " Amara ", "scores": "92,85,78"},
        {"name": "Leo", "scores": "88,91,73"},
        {"name": "Priya", "scores": "65,72,150"},         
        {"name": "Sam", "scores": "70,not_a_number,60"},  
        {"name": "Amara", "scores": "95,90,88"},          
        {"name": "Jade", "scores": "81,77,84,90"},
    ]

    students, failures = clean_and_build_students(raw_rows)