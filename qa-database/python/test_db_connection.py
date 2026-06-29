from qa_database.python.db_connection import connection

def test_user_exists();
    cursor = connection.cursor()

    cursor.execute(
         "SELECT full_mame FROM isers WHERE id = 1;"
    )

    result = cursor.fetchone()

    assert result[0] == "Bruno Barreto"

    cursor.close()
