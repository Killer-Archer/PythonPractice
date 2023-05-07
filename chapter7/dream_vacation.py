polling = True

while polling:
	name = input("What is your name?\nAns:")
	dream_place = input(f"Which is your dream place: ")
	add_ons = input("Would you like anyone else? ")

	if add_ons.lower() == 'no':
		polling = False
