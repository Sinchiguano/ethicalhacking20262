# Linux Command Line + Python
# First Python Example

import os

print("================================")
print("   PYTHON + LINUX TERMINAL")
print("================================")

name = input("Enter your name: ")

print("\nHello,", name)
print("Welcome to Linux and Python!")

print("\nCurrent directory:")
os.system("pwd")

print("\nCurrent user:")
os.system("whoami")

print("\nFiles in this directory:")
os.system("ls")

print("\nLinux system information:")
os.system("uname -a")

print("\nToday's date:")
os.system("date")

print("\n================================")
print("Program finished!")
print("================================")