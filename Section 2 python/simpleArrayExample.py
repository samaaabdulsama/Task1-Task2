#create an array in python
arr_fruits = ["Apple" , "banana", "kiwi"]
#access the element of an array
print(arr_fruits[0]) #Apple 
print(arr_fruits[1]) #banana 
print(arr_fruits[2]) #kiwi
#find the length of an array
print(len(arr_fruits)) 
#Adding array element:
arr_fruits.append("grapes") 
print(arr_fruits)
#deleting array element using index:
arr_fruits.pop(1) 
print(arr_fruits)
#deleting array element using value:
arr_fruits.remove("kiwi")
print(arr_fruits)