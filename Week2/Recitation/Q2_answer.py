# Take two string inputs from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Split the strings into lists of words
list1 = string1.split() # or string1.split(" ")
list2 = string2.split() # or string2.split(" ")

# Convert lists into sets to find common elements
set1 = set(list1)
set2 = set(list2)

"""
# we could also use a loop for the above part
set1 = set()
for elem in list1:
    set1.add(elem)

set2 = set()
for elem in list2:
    set2.add(elem)
"""

# Find the common elements using set intersection
common_elements = set1.intersection(set2)

# Print the result
print("Common elements:", common_elements)
print("Number of common elements:", len(common_elements))