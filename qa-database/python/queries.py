from db_connection import get_connection

def get_all_users():
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
	"SELECT * FROM users;"
    )

    users = cursor.fetchall()

    cursor.close()
    connection.close()

    return users

def get_user_by_id(user_id):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE id = %s;",
        (user_id,)
    )

    user = cursor.fetchone()

    cursor.close()
    connection.close()

    return user

def create_user(full_name, email):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO users
        (full_name, email)
        VALUES (%s, %s)
        RETURNING id;
        """,
        (full_name, email)
    )

    user_id = cursor.fetchone()[0]

    connection.commit()

    cursor.close()
    connection.close()

    return user_id

def deactivate_user(user_id):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE users
        SET active = FALSE
        WHERE id = %s;
        """,
        (user_id,)
    )

    connection.commit()

    cursor.close()
    connection.close()

def delete_user(user_id):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM users
        WHERE id = %s;
        """,
        (user_id,)
    )

    connection.commit()

    cursor.close()
    connection.close()

def user_exists(user_id):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE id = %s;
        """,
        (user_id,)
    )

    user = cursor.fetchone()

    cursor.close()
    connection.close()

    return user is not None
