class User:
    def __init__(self, name, email):
        self.name=name
        self.email=email
        print(f"User created: {self.name}, {self.email}")
        print("*******************************************")

    def display(self):
        return f"Name:{self.name} - Email:{self.email}"
    



student1 = User("Alice", "alice@example.com")
student2 = User("Bob", "bob@example.com")

# tmp=student1.display()
# print(tmp)





