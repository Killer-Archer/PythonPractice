sandwichs_available = ["chicken cheese", "pastrami" ,"chicken kemma", "pastrami","some cheese", "panneer" , "pastrami"]
finished_sandwichs = []

while sandwichs_available:
	for sandwich in sandwichs_available:
		if sandwich == "pastrami":
			sandwichs_available.remove(sandwich)
		else:
			print(f"I made your {sandwich}")
			finished_sandwichs.append(sandwich)
			sandwichs_available.remove(sandwich)

print("\n\nFinished Sandwiches list:")
for sandwich in finished_sandwichs:
	print(f"\t\t\t {sandwich}")
		
		

	