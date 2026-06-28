from qa_api.clients.posts_client import get_post
from qa_api.utils.api_assertions import (
    validate_status_code,
    validate_json_field,
)

def test_get_post_by_id():
    response = get_post(1)

    body = response.json()

    validate_status_code(response, 200)

    validate_json_field(body, "id", 1)
    validate_json_field(body, "userId", 1)
