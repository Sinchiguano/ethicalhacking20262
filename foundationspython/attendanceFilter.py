
# The exercise says:

# Given a list of dictionaries with "name" and "present" (True/False), print only the names of absent students.

# The main concepts are:

# list of dictionaries
# boolean values: True and False
# for loop
# if
# filtering data

# We can start with this data:

students = [
    {"name": "Alice", "present": True},
    {"name": "Bob", "present": False},
    {"name": "Charlie", "present": True},
    {"name": "David", "present": False},        
    {"name": "Eve", "present": True}  ]


# Now we can use a for loop to iterate through the list of students and check if they are absent (present == False). If they are absent, we will print their name.
for student in students:
    if not student["present"]:
        print(student["name"])
        