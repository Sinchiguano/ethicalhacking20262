import mysql.connector


connection=mysql.connector.connect(
    host="localhost",
    user="ethical_user",
    password="Ethical123!",
    database="ethical_hacking"
)




cursor=connection.cursor(dictionary=True)


sql="""INSERT INTO vulnerabilities 
(title, category, severity)
VALUES(%s,%s, %s)
"""

values=("Cross-site Scripting", "Web Application", "High")
cursor.execute(sql,values)


connection.commit()

print("Vulnerability added successfully!")