from queries import get_user_by_id

def test_fixture_user(test_user):

    user = get_user_by_id(test_user)

    assert user is not None
    assert user[1] == "Fixture User"
