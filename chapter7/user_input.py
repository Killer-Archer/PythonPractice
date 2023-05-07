#7.1
car_name = input("What car are you looking for: ")

print(f"Let me see if i can find you a {car_name}")

#7.2
no_of_people = int(input("\nHow many people are in the dinner group?\nAns: "))

if no_of_people > 8:
	print("You will have to wait some time for a table")
else:
	print("The table is ready")

#7.3
multiple = int(input("\nEnter a number multiple of 10: "))
if multiple % 10 == 0:
	print(f"{multiple} is multiple of 10")
else:
	print(f"{multiple} is not a multiple of 10")

#7.4
while True:
	print("\nEnter 'quit' if you want end the pizza toppings")
	pizza_topping = input("Enter the pizza topping which needs to be added: ")
	if pizza_topping == 'quit':
		break
	else:
		print(f"{pizza_topping} topping added")

#7.5
inc = 0
active = True
while active:
	inc += 1
	persons_age = int(input("\nEnter your age: "))
	if persons_age <= 3 :
		print("The Tickets is free\n")
	elif 3 < persons_age <= 12 :
		print("That will be $10\n")
	elif persons_age > 12 :
		print("That will be $15\n")
	
	if inc == 3 :
		print("Housefull")
		active = False

