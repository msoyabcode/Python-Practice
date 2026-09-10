# Create a set containing duplicate values and observe the output.
# st = {2,2, 4,1,2,3,3,4}
# print(st)



# Find common elements between two sets.
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# print(set1.intersection(set2))



# Find elements that are present in the first set but not in the second set.

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# print(set1.difference(set2))



# Convert a list with duplicate values into a set.
# lst = [1, 2, 3, 4, 5, 2, 3, 4]
# print(set(lst))


# Check whether one set is a subset of another set.

SetA = {1, 2, 3}
SetB = {1, 2, 3, 4, 5}

print(SetA.issubset(SetB))