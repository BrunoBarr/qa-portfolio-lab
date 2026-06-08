status_codes = [200, 201, 404, 500]

for code in status_codes:
	print(f"Validating status code: {code}")

	if code < 400:
		print("Success")
	else:
		print("Failure")
