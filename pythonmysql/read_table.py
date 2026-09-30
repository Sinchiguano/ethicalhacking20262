import mysql.connector


connection=mysql.connector.connect(
    host="localhost",
    user="ethical_user",
    password="Ethical123!",
    database='ethical_hacking'
)



# cursor=connection.cursor()
# cursor.execute('SELECT * FROM vulnerabilities')
# vulnerabilities=cursor.fetchall()

# for vulnerability in vulnerabilities:
#     print(vulnerabilities)





cursor=connection.cursor(dictionary=True)
cursor.execute('SELECT * FROM vulnerabilities')
vulnerabilities=cursor.fetchall()

for vulnerability in vulnerabilities:
    print(vulnerabilities)
    