
# def greet():
#     print("Hello, world!")

# # greet( )

# message=greet

# message()
# print('///////////////')
# print(greet)
# print('///////////////')
# print(greet())



# print("show that a function can receive another function")

# def execute_function(func):
#     func()  

# execute_function(greet)


# """ In Python, functions can be treated like variables."""
# print(" In Python, functions can be treated like variables.")

# def greetings(name):
#     return f"Hello, {name}"


# messageName=greetings


# print(messageName("Bob"))
# print(messageName("David"))
# print(messageName("Charlie"))


# def my_decorator(func):
#     def wrapper():
#         print("before the function")
#         func()
#         print("after the function")
#     return wrapper



# def greet():
#     print("Hello students")


# greet=my_decorator(greet)

# greet()

from flask import Flask
app=Flask(__name__)



@app.route('/')
def home():
    return 'Hello, World!'


@app.route("/admin")
def admin():
    return "Admin page"

if __name__=="__main__":
    app.run(debug=True)
    