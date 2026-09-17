# Create 3 User objects, put them in a list, and loop through calling display() on each.


class User:
    def __init__(self, name, email):
        self.name=name
        self.email=email
        # print(f"User created: {self.name}, {self.email}")
        # print("*******************************************")

    def display(self):
        return f"Name:{self.name} - Email:{self.email}" 




user1 = User("Alice", "alice@example.com")
user2 = User("Bob", "bob@example.com")
user3 = User("Charlie", "charlie@example.com")


users = [user1, user2, user3]

for user in users:
    print(user.display())
