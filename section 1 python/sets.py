#Sets
# Example set of numbers
my_set = {1, 2, 3, 4, 5}

# Example set of strings (duplicates are automatically removed)
letters ={"a" ,"b","c"}
print(letters)
unique_letters = {"a", "b", "c", "a", "d"}
print(unique_letters) # Output: {'d', 'a', 'c', 'b'} (order may vary)

# Adding elements
my_set.add(6)
print(my_set) # Output: {1, 2, 3, 4, 5, 6}

# Removing elements
my_set.remove(1)  #take value not index
print(my_set) # Output: {2, 3, 4, 5, 6}
letters.remove("a")
print(letters)