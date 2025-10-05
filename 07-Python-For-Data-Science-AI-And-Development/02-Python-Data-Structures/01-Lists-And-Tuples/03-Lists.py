# Create a list
L = ["The Bodyguard", 7.0, 1992]
print(L)

# Print the elements on each index
print('The same element using negative and positive indexing:\nPositive: ', L[0], '\nNegative: ', L[-3])
print('The same element using negative and positive indexing:\nPositive: ', L[1], '\nNegative: ', L[-2])
print('The same element using negative and positive indexing:\nPositive: ', L[2], '\nNegative: ', L[-1])

# Sample list
print(["The Bodyguard", 7.0, 1992, [1, 2], ("A", 1)])

# Sample list
L = ["The Bodyguard", 7.0, 1992, "BG", 1]
print(L)

# List slicing
print(L[3:5])

# Use extend to add elements to list
L = ["The Bodyguard", 7.0]
print(L)
L.extend(['pop', 10])
print(L)

# Use append to add elements to list
L = ["The Bodyguard", 7.0]
print(L)
L.append(['pop', 10])
print(L)

# Use extend to add elements to list
L = ["The Bodyguard", 7.0]
print(L)
L.extend(['pop', 10])
print(L)

# Use append to add elements to list
L.append(['a', 'b'])
print(L)

# Change the element based on the index
A = ["disco", 10, 1.2]
print("Before change: ", A)
A[0] = "hard rock"
print("After change: ", A)

# Delete the element based on the index
print("Before change: ", A)
del(A[0])
print("After change: ", A)

# Split the string, default is by space
print('hard rock'.split())

# Split the string by comma
print('A,B,C,D'.split(','))

# Copy and Clone List

# Copy (copy by reference) the list A
A = ["hard rock", 10, 1.2]
B = A
print('A: ', A)
print('B: ', B)

# Examine the copy by reference
print('B[0]: ', B[0])
A[0] = 'banana'
print('B[0]: ', B[0])

# Clone (clone by value) the list A
B = A[:]
print(B)

# Now if you change A, B will not change
print('B[0]: ', B[0])
A[0] = 'hard rock'
print('B[0]: ', B[0])

# EXERCISES
a_list = [1, 'hello', [1, 2, 3], True]
print(a_list)

print(a_list[1])

print(a_list[1:4])

A = [1, 'a']
B = [2, 1, 'd']
print(A + B)

# Create an empty list
Shopping_list = []

# Now store the number of items to the shopping list
Shopping_list = ["Watch", "Laptop", "Shoes", "Pen", "Clothes"]

# Add a new item to the shopping_list
Shopping_list.append("Football")

# Print first item from the shopping_list
print(Shopping_list[0])

# Print last item from the shopping_list
print(Shopping_list[5])

# Print the entire Shopping List
print(Shopping_list)

# Print the item that are important to buy from the shopping list
print(Shopping_list[1:3])

# Change the item from the shopping_list
Shopping_list[3] = "Notebook"

# Delete the item from the shopping_list that is not required
del(Shopping_list[4])

# Print the shopping_list
print(Shopping_list)