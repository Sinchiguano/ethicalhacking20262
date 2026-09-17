# Create Admin(User) that adds a role="admin" attribute and overrides display() to show the role too.
class User:
    def __init__(self, name, email):
        self.name=name
        self.email=email
        # print(f"User created: {self.name}, {self.email}")
        # print("*******************************************")

    def display(self):
        return f"Name:{self.name} - Email:{self.email}"



class Admin(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.role = "admin"
        # print(f"Admin created: {self.name}, {self.email}, Role: {self.role}")
        # print("*******************************************")

    def display(self):
        # return f"Name:{self.name} - Email:{self.email} - Role:{self.role}"
        return f"{super().display()} - Role:{self.role} "


admin1 = Admin("Charlie", "charlie@example.com")
print(admin1.display())
user1 = User("David", "david@example.com")
print(user1.display())