import sys
argv = sys.argv[1]

if argv == "Restaurant":
	class Restaurant():

		def __init__(self, restaurant_name, cuisine_type):
			self.restaurant_name = restaurant_name
			self.cuisine_type = cuisine_type
			self.number_served = 0
			self.login_attempts = 0

		def describe_restaurant(self):
			print(f"{self.restaurant_name.title()} restaurant serves {self.cuisine_type} cuisine")

		def open_restaurant(self):
			print(f"{self.restaurant_name.title()} restaurant is open from 9:00 to 12:00")

		def read_number_served(self):
			print(f"{self.restaurant_name.title()} restaurant has served {self.number_served} customers")

		def read_login_attempts(self):
			print(f"Login Attempts = {self.login_attempts}")

		def set_number_served(self,customer_served):
			self.number_served = customer_served

		def increment_number_served(self,customer_served):
			self.number_served += customer_served

		def increment_login_attempts(self):
			self.login_attempts += 1

		def reset_login_attempts(self):
			self.login_attempts = 0


	#First Instance
	restaurant = Restaurant("Biryani Type", "Indian")
	print(restaurant.restaurant_name)
	print(restaurant.cuisine_type)
	restaurant.describe_restaurant()
	restaurant.open_restaurant()

	#Second Instance
	restaurant_2 = Restaurant("Taco Bell", "Indian")
	restaurant_2.describe_restaurant()

	#Third Instance
	restaurant_3 = Restaurant("KFC", "American")
	restaurant_3.describe_restaurant()

	#Fourth Instance
	print("\nForth Instance for attribute testing\n")
	restaurant_4 = Restaurant("Wendys", "American")
	restaurant_4.read_number_served()
	restaurant_4.number_served = 50
	restaurant_4.read_number_served()

	#Calling the method Set Number Served
	print("\nUpdating the Number of customer served through method\n")
	restaurant_4.set_number_served(100)
	restaurant_4.read_number_served()

	#Calling the method increment number served
	print("\nUpdating the customer served through increment method")
	restaurant_4.increment_number_served(100)
	restaurant_4.read_number_served()

	#Testing Login attempts functions
	print("\nTesting method login attempts\n")
	restaurant_4.increment_login_attempts()
	restaurant_4.increment_login_attempts()
	restaurant_4.read_login_attempts()
	restaurant_4.reset_login_attempts()
	restaurant_4.read_login_attempts()
elif argv == "User":
	class Users():

		def __init__(self,first_name,last_name,**user_data):
			self.first_name = first_name
			self.last_name = last_name
			self.user_data = user_data

		def describe_user(self):
			self.profile = {}
			self.profile['first_name'] = self.first_name
			self.profile['last_name'] = self.last_name
			for self.key,self.value in self.user_data.items():
				self.profile[self.key] = self.value
			return self.profile

		def greet_user(self):
			print(f"Hello {self.first_name.title()} {self.last_name.title()}")

	#First Instance
	user = Users("Rahul","Dravid",matches=150,Runs=5000)
	print(f"{user.first_name.title()} User Details\n")
	User_data = user.describe_user()
	print(User_data)
	user.greet_user()

	#Second Instance
	user_1 = Users("Virat","Kohli",century=75,franchise_name = "RCB")
	print(f"\n{user_1.first_name.title()} User Details\n")
	User_data = user_1.describe_user()
	print(User_data)
	user_1.greet_user()

	#Third Instance
	user_2 = Users("AB", "De villers", Breed = "Alien", franchise_name = "RCB")
	print(f"\n{user_2.first_name.title()} User Details\n")
	User_data = user_2.describe_user()
	print(User_data)
	user_2.greet_user()
else:
	class Dog():

		def __init__(self, name, age):
			self.name = name
			self.age = age

		def sit(self):
			print(f"{self.name.title()} is not sitting")

		def roll_over(self):
			print(f"{self.name.title()} rolled over")

	my_dog = Dog("Mikey",23)
	my_dog_1 = Dog("Draken", 25)
	my_dog.sit()
	my_dog_1.roll_over()
	print(my_dog.name)
	print(my_dog)
	print(my_dog_1)



