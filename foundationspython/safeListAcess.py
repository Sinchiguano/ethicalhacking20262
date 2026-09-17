# Write get_item(lst, index) that returns None instead of crashing when the index is out of range.

colors = ['red', 'green', 'blue']
def get_item(lst, index):
    try:
        return lst[index]
    except IndexError:
        return None

print(get_item(colors, 0))  # Output: red
print(get_item(colors, 5))  # Output: None



items = ["keyboard", "mouse", "monitor"]

print(get_item(items, 1))
print(get_item(items, 10))