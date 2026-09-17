# Write find_user_by_email(users, email) using next(), returning None if not found.

users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

def find_user_by_email(users, email):
    return next((user for user in users if user["email"] == email), None)

# find_user_by_email(users, "alice@example.com")
print(find_user_by_email(users, "alice@example.com"))

