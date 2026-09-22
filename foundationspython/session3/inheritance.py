# Create Admin(User) that adds a role='admin' attribute and overrides display() to show the role.

print("----- User Class -----")
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display(self):
        return f"Name: {self.name} - Email: {self.email}"

user1 = User("Cesar", "cesar.sinchiguano@gmail.com")
user2 = User("Jeremy", "jeremy.guerrero@gmail.com")
user3 = User("Danilo", "danilo.mendoza@gmail.com")  
print(user1.display())
print(user2.display())
print(user3.display())  

print("----- Admin Users -----")


class Admin(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.role = 'admin'     
    def display(self):
        return f"{self.name}, {self.email}, {self.role}"



user4 = Admin("AdminUser", "adminuser@gmail.com")
user5 = Admin("AdminUser2", "adminuser@gmail.com")
print(user4.display())
print(user5.display())



        