import time
#Count from 1 to 20

for number in range(1,21):
	print(number)

#print list consisting number 1 to million

one_to_millions = list(range(1,1000000))
# for value in one_to_millions:
# 	print(value)

#Find min in million and find the sum of million

print("\nMinimum value in the list = ",min(one_to_millions))
start_time = time.time()
summation_of_millions = sum(one_to_millions)
end_time = time.time()
time_taken = end_time - start_time
print(f"\nIt took {time_taken} seconds to sum the values in the list of numbers and sum = {summation_of_millions}")

#Creating a list with odd numbers

odd_numb_list = list(range(1,20,2))
print(f"List of odd numbers = {odd_numb_list}")

#Multiple of 3 to 30

multiples_of_3 = list(range(3,31,3))
print(f"\nMultiple of 3 list = {multiples_of_3}")

#List with cubes of number
cubes_of_number = [value**3 for value in range(1,10)]
print(f"\nList of cubes of number = {cubes_of_number}")


#Slicing

print(f"First three items of list's are = {cubes_of_number[:3]}")
middle = len(cubes_of_number)//2
print(f"\nThree elements from middle of list are = {cubes_of_number[middle:middle+3]}")
print(f"\nLast three elements of the list are = {cubes_of_number[-3:]}")