import psycopg2

def get_connection():
    connection = psycopg2.connect(
        host="localhost",
        database="qa_lab",
        user="qa_user",
        password="qa_password"
    )

    return connection
