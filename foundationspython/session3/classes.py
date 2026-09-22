
class User:
    def __init__(self, name,email):
        self.name=name
        self.email=email

        # print("User Created")
    def show_information(self):
        return f"name:{self.name}, email:{self.email}"


user1=User("Cesar","cesar.sinchiguano@gmail.com")
user2=User("Jeremy","jeremy.sample@gmail.com")
user3=User("Danilo","danilo.sample@gmail.com")


# tmp=user1.show_information()
# print(tmp)

print(user2.show_information())
print(user3.show_information())
