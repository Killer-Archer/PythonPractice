current_users = ["KOHLI","naveen","mishra","mayers","gautam"]

new_users = ["kohli","siraj","harshal","lomror","prabhudesai"]

for new_user in new_users:
	if new_user.upper() in current_users:
		print(f"\n {new_user} will need to enter a new username")
	else:
		print(f"\n {new_user} name is available")