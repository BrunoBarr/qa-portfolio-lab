import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="qa_lab",
    user="qa_user",
    password="qa_password"
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM users;")

users = cursor.fetchall()

for user in users:
    print(user)

cursor.close()
connection.close()
