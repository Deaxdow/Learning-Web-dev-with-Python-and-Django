#lists
"""
fruits = ["apple", "banana", "cherry"]
print(fruits)
"""
#List Methods
"""
fruits.append("orange")
print(fruits)

fruits.remove("orange")
print(fruits)

fruits.pop()
print(fruits)

fruits.insert(1, "Guava")
print(fruits)


fruits.extend(["mango", "pineapple"])
print(fruits)


print(fruits.count("apple"))
print(fruits)

"""


"""
numbers = [1, 2, 3, 4, 5]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(len(numbers))
print(numbers[0])
"""


#List slicing
"""
colors = ["red", "green", "blue"]
print(colors[0:1])
"""



##Tuples
"""
fruits = ("apple", "banana", "cherry")
print(fruits[0])
print(fruits)
"""


"""
#Tuple methods
fruitsTuple = ("apple", "banana", "cherry")
#Tuple convert to list
fruitsList=list(fruitsTuple)
print(fruitsList)

#List convert -> to tuple
fruitsTuple = tuple(fruitsList)
print(fruitsTuple)
"""

#SETS

"""
#Sets
fruits = {"apple", "banana", "cherry", "apple"}
#Set methods
fruits = {"apple", "banana", "cherry", "apple"}
fruits.add("orange")
print(fruits)

fruits.remove("orange")
print(fruits)

fruits.update(["mango", "pineapple"])
print(fruits)

fruits.pop()
print(fruits)

fruits.clear()
print(fruits)



#Set union

set1 = {1, 2, 3}
set2 = {4, 5, 6}
result = set1.union(set2)
print(result)

#Set intersection

set1 = {1, 2, 3}
set2 = {3, 5, 6}

result = set1.intersection(set2)
print(result)

#set diff
set1 = {1, 2, 3}
set2 = {3, 5, 6}
result = set1.symmetric_difference(set2)
print(result)
"""

