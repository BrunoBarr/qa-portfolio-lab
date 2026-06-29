from queries import (
    get_all_users,
    get_user_by_id,
    create_user
)

def test_users_exist():
    users = get_all_users()

    assert len(users) > 0

def test_get_user_by_id():
    user = get_user_by_id(1)

    assert user[1] == "Bruno Barreto"
    assert user[2] == "bruno@test.com"
    assert user[3] is True

def test_create_user():

    user_id = create_user(
        "Pytest User",
        "pytest@test.com"
   )

    user = get_user_by_id(user_id)

    assert user[1] == "Pytest User"
    assert user[2] == "pytest@test.com"
    assert user[3] is True
