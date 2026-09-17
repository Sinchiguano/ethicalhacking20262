# filtering with comprehension


users=[{'id':1,'name':'Alice','role':'admin'}, 
       {'id':2,'name':'Bob','role':'user'},
       {'id':3,'name':'Charlie','role':'admin'},
       {'id':4,'name':'David','role':'user'}]



# filters admin

admins=[user for user in users if user['role']=='admin']

print(admins)


print("*******************************************")
print("filtering with next()")
user=next((user for user in users if user['id']==5),None)
print(user)