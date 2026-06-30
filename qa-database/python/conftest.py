import pytest
from queries import create_user, delete_user

@pytest.fixture
def test_user():

    user_id = create_user(
        "Fixture User",
        "fixture@test.com"
    )

    yield user_id

    delete_user(user_id)
