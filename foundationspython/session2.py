
def greetings(name):
    return print(f'Hello {name}!!!')






greetings('Cesar')


def divide(a,b):
    if b==0:
        return print("Division by zero is not allowed")
    return print((f'{a} divided by {b} is {a/b}'))



divide(20,3)

print("***************")
print()


# try:
#     number=int(input("Enter a number:"))
#     print(f'You entered: {number}')

# except ValueError:
#     print("Invalid input. Please enter a valid interger.")

try:
    result=10/int(input("Enter a number:"))
except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    print("Invalid input, that is not a number.")




# number=int(input("Enter a number:"))
# print(f'You entered: {number}')


# print("Invalid input. Please enter a valid interger.")
