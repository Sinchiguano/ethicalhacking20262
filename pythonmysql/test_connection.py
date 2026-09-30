import mysql.connector


connection=mysql.connector.connect(
    host='localhost',
    user='ethical_user',
    password='Ethical123!',
    database='ethical_hacking'
)


if connection.is_connected():
    print('Connected successfully to MySql')
else:
    print('Failed to connect to MySql')


connection.close()

