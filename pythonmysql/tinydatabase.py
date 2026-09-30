import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="ethical_user",
    password="Ethical123!",
    database="ethical_hacking"
)


cursor = connection.cursor()


print("=== Ethical Hacking Vulnerability Tracker ===")


title = input("Vulnerability title: ")
category = input("OWASP category: ")
severity = input("Severity: ")


sql = """
INSERT INTO vulnerabilities
(title, category, severity)
VALUES (%s, %s, %s)
"""


values = (
    title,
    category,
    severity
)


cursor.execute(sql, values)

connection.commit()


print()
print("Vulnerability registered successfully.")


cursor.close()
connection.close()