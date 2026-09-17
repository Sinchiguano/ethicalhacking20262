
from utils import is_valid_email

email = input("Enter your email address: ")
if is_valid_email(email):
    print("Valid email address.")
else:
    print("Invalid email address.") 