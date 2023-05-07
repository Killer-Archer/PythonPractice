programming_terms = {
    "print": "This method is used to display output on the console.",
    "len": "This method is used to find the length of a string, list, tuple, dictionary, or any other iterable object.",
    "str": "This method is used to convert any data type to a string.",
    "int": "This method is used to convert a string or a float to an integer.",
    "float": "This method is used to convert a string or an integer to a floating-point number.",
    "type": "This method is used to find the type of data stored in a variable or object.",
    "range": "This method is used to generate a range of numbers from a start value to an end value with a given step size.",
    "input": "This method is used to take input from the user in the console.",
    "split": "This method is used to split a string into a list of substrings based on a delimiter.",
    "join": "This method is used to join a list of strings into a single string with a given delimiter.",
    "strip": "This method is used to remove whitespace characters from the beginning and end of a string.",
    "replace": "This method is used to replace a substring in a string with another substring.",
    "append": "This method is used to add an element to the end of a list.",
    "pop": "This method is used to remove the last element from a list."}

for key in sorted(programming_terms.keys()):
    print(f"{key.title()} : {programming_terms[key]}")
 	