import requests

def test_invalid_post():
	response = requests.get(
	"https://jsonplaceholder.typicode.com/posts/999999"
	)

	assert response.status_code == 404
