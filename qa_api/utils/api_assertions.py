def validate_status_code(response, expected_status):
    assert response.status_code == expected_status

def validate_json_field(body, field, expected_value):
    assert body[field] == expected_value
