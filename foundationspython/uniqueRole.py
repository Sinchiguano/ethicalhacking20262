# Given a list of user dictionaries, build a list of the distinct "role" values without using set() — just a for loop and an if check.

users = [
    {"name": "Alice", "role": "admin"},
    {"name": "Bob", "role": "user"},
    {"name": "Charlie", "role": "admin"},
    {"name": "David", "role": "user"},
    {"name": "Eve", "role": "moderator"},
]
unique_role=[]
for user in users:
    if user["role"] not in unique_role:
        unique_role.append(user["role"])

print(unique_role)