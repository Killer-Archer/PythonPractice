places = ["Russia","Canada","UAE","New Zealand","Australia"]

print("Original List order = ",places)

print("\nSorted List order = ",sorted(places))

print("\n Order of list is retained even after using sorted function", places)

print("\n Printing the list in reversed order=",sorted(places,reverse=True))

print("\n Order of list is retained even after using sorted function", places)

places.reverse()

print("\n Order of the list using reverse method = ",places)

places.reverse()

print("\n Reversing the order of list on top of reverse method = ",places)

places.sort()

print("\n Sorted in alphabetical order = ",places)

places.sort(reverse=True)

print("\n Sorted in Reverse alphabetical order = ",places)