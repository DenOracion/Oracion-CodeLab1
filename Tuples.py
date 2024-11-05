#Creating a tuple
fruits = ('apple', 'banana', 'cherry')
print(fruits[1])
print(fruits[-1])

colors = ('red', 'green', 'blue')
colors1, colors2, colors3 = colors
print(colors1)
print(colors2)
print(colors3)

#Tuple Concatenation
numbers1 = (1, 2, 3)
numbers2 = (4, 5, 6)
numbers_combined = numbers1 + numbers2
print (numbers_combined) #output: (1, 2, 3, 4, 5, 6)

#Tuple Slicing
alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
print(alphabet[:3]) # output: ('a', 'b', 'c')
print(alphabet[-3:]) # output: ('e', 'f', 'g')
print(alphabet[::2]) # output: ('a', 'c', 'e', 'g')

#Tuple Methods
numbers = (1, 2, 2, 3, 4, 4, 4, 5)
print(numbers.count(4)) # Output: 3
print(numbers.index(2)) # Output: 1

#Nested tuples
nested = (1, 2, (3, 4), 5)
print(nested[2][1]) # output: 4

#Tuple membership testing
colors = ('red', 'green', 'blue')
print('yellow' in colors) #output: false
print('blue' in colors) #output: true