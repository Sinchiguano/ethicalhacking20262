
# name="Cesar"

# age=25

# active=True


# # IF CONDICTIONALS
# if age>20:
#     print('You are an adult person!!!')

# #CONTROL LOOPS
# for i in range(5):
#     print(i)


# # LISTS
# students=['Ana','Luis','Carlos']

# for name in students:
#     print(f' {name} student is in ethical hacking class')



# # DICTIONARIES
# user={
#     'id1':'Ana',
#     'age1':23,
#     'id2':'Cesar',
#     'age2':25
# }

# print(user['id1'])
# print(user['age1'])


# for key, value in user.items():
#     print(f'{key}: {value}')

print('#################')

students = [
    {"name": "Alice", "grade": 90},
    {"name": "Bob", "grade": 85},
    {"name": "Charlie", "grade": 92},
    {"name": "Diana", "grade": 88}
]

for student in students:
    if student['grade']>=70:
        print(student['name'], "PASS")
    else:
        print(f'{student["name"]}, FAIL.....')


print('///////////////')
print()
print('-----------------------')

for i in range(20):
    print(f'The actual number is {i}')
    if i%2==0:
        print(f'The number {i} is even!!!')

    else:
        print(f'The number {i} is odd!!!')
