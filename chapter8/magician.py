def show_magicians(magicians):
	for magician in magicians:
		print(f"{magician}")

def make_great(magicians):
	for index in range(len(magicians)):
		magicians[index] = f"Great {magicians[index]}"
	show_magicians(magicians)

magicians = ["Hastar","bastar"]
make_great(magicians[:])
show_magicians(magicians)

