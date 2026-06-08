def validate_status(status_code):
	return status_code == 200

print(validate_status(200))
print(validate_status(404))
