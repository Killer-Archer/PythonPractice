def dinner_invitation(invited_guest):
	for i in invited_guest:
		print(f"Hello {i}, I would like you to join me on a dinner tonight")

names = ["Chadwick", "Sushanth", "SPB"]

dinner_invitation(names)

print(f"\n{names[0]} won't be joining.\n")

names[0] = "Samantha"

dinner_invitation(names)

print("\nUpdated Invitation\n")

print("\nI would like to inform everyone i have got a bigger table for dinner\n")

names.insert(0,"Chadwick")
middle_index = len(names)//2
names.insert(middle_index,"ABD")
names.append("Virat Kohli")

dinner_invitation(names)

print("\nSeems like the dinner table won't be delivered in time, I would only have room for two\n")

while len(names)!=2:
	guest = names.pop()
	print("\nI wanted you to inform we can't accomodate you to the dinner tonight",guest)

print("\nUpdated Invitation\n")

print(f"\nNumber of people invited = {len(names)}\n")

dinner_invitation(names)

del names[0]
del names[0]

print(names)

