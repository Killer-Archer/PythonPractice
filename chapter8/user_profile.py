def build_profile(first_name,last_name,**user_data):
	profile = {}
	profile['first_name'] = first_name
	profile['last_name'] = last_name

	for key,value in user_data.items():
		profile[key] = value

	return profile


user_profile = build_profile("Wriddiman", "Saha", Runs = "81", Sixes = 10, fours = 63)

print(user_profile)