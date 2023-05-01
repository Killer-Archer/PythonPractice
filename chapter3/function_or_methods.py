some_list =["Mountain", "Host","People","Death"]

def user_defined_print(string_to_print,variable_to_print):
	print(f"{string_to_print} = {variable_to_print}\n")

user_defined_print("Lenght of the list",len(some_list))
user_defined_print("List after poping a element",some_list.pop())
user_defined_print("First element of the list",some_list[0])
user_defined_print("Removing the first element of the list",some_list.pop(0))
some_list.append("Sun")
user_defined_print("Adding a element to the list",some_list)
some_list.insert(0,"Moon")
user_defined_print("Adding an element to begining of the list",some_list)
some_list.sort()
user_defined_print("Sorting the list in alphabetical order",some_list)
some_list.sort(reverse=True)
user_defined_print("Sorting the list in reverse alphabetical order",some_list)
some_list.reverse()
user_defined_print("Sorting the list using reverse function",some_list)