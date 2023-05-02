users = ["admin","negrok","manuaha","paresh","kongesh"]
if users:
	for user in users:
		if user == "admin":
			print("Hello admin, would you like a status report")
		else:
			print(f"\nHello {user}, thankyou for logging in")
else:
	print("We need some Users")

	