# Ask the user for a number and print its multiplication table from 1 to 10 using a for loop.



number=int(input("Enter a number: "))

for i in range (1, 11):
    print(f"{number} x {i} = {number * i}")
    