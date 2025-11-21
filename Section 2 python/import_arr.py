import array as arr
# Create an array of signed integers ('i' type code)
my_array = arr.array('i', [10, 20, 30, 40, 50]) # i refers to integer value

# Accessing elements
print(f"First element: {my_array[0]}") #f refers to formating string => appling {}
print(f"Third element: {my_array[2]}")

# Modifying an element
my_array[1] = 25
print(f"Modified array: {my_array}")

# Adding elements
my_array.append(60)
print(f"Array after appending: {my_array}")

my_array.insert(2, 35) # Insert 35 at index 2
print(f"Array after inserting: {my_array}")

# Removing elements
my_array.pop() # Removes the last element
print(f"Array after popping: {my_array}")

my_array.remove(30) # Removes the first occurrence of 30
print(f"Array after removing 30: {my_array}")

# Iterating through the array
print("Elements in the array:")
for x in my_array:
    print(x)