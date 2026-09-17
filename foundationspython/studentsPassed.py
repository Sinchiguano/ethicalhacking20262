# From a list of {name, grade} dictionaries, build a list of names with grade >= 7 using a comprehension.

students = [
    {"name": "Alice", "grade": 8},
    {"name": "Bob", "grade": 6},        
    {"name": "Charlie", "grade": 7},
    {"name": "David", "grade": 5},
    {"name": "Eve", "grade": 9}
]

passed_students = [student["name"] for student in students if student["grade"] >= 7]
print(passed_students)