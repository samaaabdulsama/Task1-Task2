#syntax
#lambda argument: expression 
add = lambda x,y : x+y
print(add(3,5))
# lambda function can have any number of parameters, but only one expression. 
# lambda function can have zero or more number of parameters
# The expression is automatically returned (no need for return). 
#Lambda functions are frequently used as arguments to higher-order functions like 
# map(), filter(), sorted(), and reduce()
# apply lambda function with map()
numbers = [1,2,3,4,5]
square = list(map(lambda x: x**2 , numbers))
print(square)
# apply lambda With filter() – Filter items based on a condition: 
#printing the even number
list_number = [1,2,3,4,5,6]
evens = list(filter(lambda x : x%2 ==0 , list_number))
print(evens)
# apply lambda With sorted() – Sort lists using a custom rule:
data = ((1,'B'),(3,'C'),(2,'A'))
lst_sorted = sorted(data , key=lambda x:x[1] )
print(lst_sorted)
# With multiple iterables in map() – Combine elements from multiple lists:
num1 = [1,2,3]
num2 =[5,6,7]
add_numbers = list(map(lambda x,y: x+y, num1,num2))
print(add_numbers)