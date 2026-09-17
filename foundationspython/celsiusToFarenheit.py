# Write a function celsius_to_fahrenheit(c) and its inverse. Handle non-numeric input with try/except.

def celsius_to_fahrenheit(c):
    try:
        f = (c * 9/5) + 32
        return f
    except TypeError:
        return "Input must be a numeric value."     

def fahrenheit_to_celsius(f):
    try:
        c = (f - 32) * 5/9
        return c
    except TypeError:
        return "Input must be a numeric value."


print(celsius_to_fahrenheit(0))
print(fahrenheit_to_celsius(32))