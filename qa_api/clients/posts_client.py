import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_post(post_id):
    response = requests.get(
	f"{BASE_URL}/posts/{post_id}"
    )

    return response
