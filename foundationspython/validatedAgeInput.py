# Write a function that keeps asking for age until a valid integer between 0 and 120 is entered.


def get_valid_age():
    while True:
        try:
            age = int(input("Please enter your age (0-120): "))
            if 0 <= age <= 120:
                return age
            else:
                print("Age must be between 0 and 120. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")   


age = get_valid_age()
print(f"Your age is: {age}")