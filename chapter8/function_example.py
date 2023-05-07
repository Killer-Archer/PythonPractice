def make_shirt(size="Large", text_printed="I Love Python"):
	print(f"{size} sized shirt is printed with {text_printed}")

def describe_city(name="Bangalore", description="best city"):
	print(f"{name} is the {description}")

def city_country(city,country):
	return f"{city.title()}, {country.title()}"

#Make shirt function calls
make_shirt("M","I am Batman")
make_shirt(text_printed="I am robin", size="S")
make_shirt()
make_shirt("M")

#describe city function calls
describe_city()
describe_city("Pune", "next best after bangalore")

#city country function calls
some_var = city_country("Bangalore","India")
some_var1 = city_country("London","England")
print(some_var)
print(some_var1)