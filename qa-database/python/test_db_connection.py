import uuid

from queries import (
    get_all_users,
    get_user_by_id,
    create_user,
    deactivate_user,
    delete_user,
    user_exists
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

    email = f"{uuid.uuid4()}@test.com"

    user_id = create_user(
        "Pytest User",
        email
    )

    user = get_user_by_id(user_id)

    assert user[1] == "Pytest User"
    assert user[2] == email

def test_deactivate_user():

    user_id = create_user(
        "Deactivate User",
        "deactivate1@test.com"
    )

    deactivate_user(user_id)

    user = get_user_by_id(user_id)

    assert user[3] is False

def test_delete_user():

    user_id = create_user(
        "Delete User",
        "delete1@test.com"
    )

    delete_user(user_id)

    user = user_exists(user_id)

    assert not user
