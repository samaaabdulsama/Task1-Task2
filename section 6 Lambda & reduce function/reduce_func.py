# apply lambda with reduce()
#reduce not a built-in function we must import it
from functools import reduce
#reduce(function , iterable)
# function like lambda 
#iterable like list or any iterable object
numbers1 = [1,2,3,4,5,6]
result = reduce(lambda x,y:x+y , numbers1)
print(result)

#Use reduce() when: 
# You want to combine all elements of a list into one result. 
# The operation is naturally cumulative (sum, product, min/max, etc.)
#find the max value
numbers2 = [10, 3, 27, 5, 18] 
max_value = reduce(lambda x, y: x if x > y else y, numbers2) 
print(max_value) 