# Define class InvalidGradeError(Exception) and raise it inside a function when a grade is outside 0–10.

class InvalidGradeError(Exception):
    """Custom exception for invalid grades."""
    pass    



def check_grade(grade):
    if not (0 <= grade <= 10):
        raise InvalidGradeError(f"Grade {grade} is invalid. Must be between 0 and 10.")
    return grade



try:
    grade = float(input("Enter a grade (0-10): "))
    valid_grade = check_grade(grade)
    print(f"Valid grade entered: {valid_grade}")
except InvalidGradeError as e:
    print(e)    
    