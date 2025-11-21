#dictionaty
# Example dictionary for a person's information
person = {
    "name": "Alice",
    "age": 19,
    "city": "New York"
}

# Example dictionary with different key and value types
student_scores = {
    "math": 95,
    "science": 88,
    "history": 72
}

# Accessing values by key
print(person["name"]) 
print(student_scores["math"]) 
print(person)
print(student_scores)
# Modifying values
person["age"] = 20
print(person) 
student_scores["science"]=97
print(student_scores)
# Adding new key-value pairs
person["level"] = "Two"
print(person) 