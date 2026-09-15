
# # int variable=10;


# #VARIABLES


# number=10

# name="Cesar Sinchiguano"

# active=True

# print("gggggg")
# if number>5:
#     print("The number is greater than 5 ")
# else:
#     print("The number is less than 5")


# for i in range(10):
#     print("The number is:",i)
#     print(f"The number is: {i}")


# students=list()
# for i in range(100):
#     students.append(i)


# for i in students:
#     print("The student number is :",i)

# names=["carlos","cesar","jose","maria"]
# for name in names:
#     print(name)


# names={"carlos":1,"cesar":2,"jose":3,"maria":4}

# print(names["jose"])

# for name in names.items():
#     print(name)

students = [
    {"name": "Ana", "score": 9.2},
    {"name": "Carlos", "score": 8.5},
    {"name": "Maria", "score": 7.8},
    {"name": "Luis", "score": 9.0},
    {"name": "Sofia", "score": 8.7},
    {"name": "Pedro", "score": 6.9},
    {"name": "Daniela", "score": 9.5},
    {"name": "Jorge", "score": 7.4},
    {"name": "Valeria", "score": 8.9},
    {"name": "Miguel", "score": 7.7}
]


print(students[2])
for name in students:
    # print(name.items())
    # print(name['score'])
    if name['score'] > 7:
        print("The student PASSED the course")
    else: 
        print("The student FAILED the course")
