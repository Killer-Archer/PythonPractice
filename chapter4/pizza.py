pizzas = ["Chicken Keema", "Chicken barbecue","Panner "]
for pizza in pizzas:
	print(f"I like {pizza} pizza")

print("I like Pizza's a lot because of cheese and topings on it with the crust giving it perfect crunch\n")
print("I really love pizza")

friend_pizzas = pizzas[:]
friend_pizzas.append("Onion Chesse")
pizzas.append("Pepper Chicken")

print(f"\nOriginal list of pizza = {pizzas}")
print(f"\nCopy of pizzas list = {friend_pizzas}")

print("\nThe First List of pizza's")
for pizza in pizzas:
	print(pizza)

print("\nCopied list of pizza's")
for pizza in friend_pizzas:
	print(pizza)