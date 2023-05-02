dimensions = (10,10)
print(dimensions[0])
print(dimensions[1])

#Assigning the value to tuples
#The below code would return an error as tuple immutable
#dimensions[0]=20

dimensions = (400,10)
print(dimensions[0])
print(dimensions[1])

#adding a element to a tuple
dimensions = dimensions + (20,)
print(f"\nAdding new elements to the tuple = {dimensions}")

Menus = ("Pizza","Burger","Biryani","Taco","Dosa")
for food in Menus:
	print(food)

print("\n")
Menus = ("Idli","Anna-Sambar","Dosa","Taco","Pizza")
for food in Menus:
	print(food)