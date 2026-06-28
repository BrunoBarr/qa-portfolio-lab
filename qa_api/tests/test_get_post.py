import requests


def test_get_post_by_id():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    body = response.json()
    print(body)

    assert response.status_code == 200
    assert body["id"] == 1
    assert body["userId"] == 1
