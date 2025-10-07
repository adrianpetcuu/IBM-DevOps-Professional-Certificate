# First function example: Add 1 to a and store as b
def add(a):
    """
    add 1 to a
    """
    b = a + 1
    print(a, "if you add one", b)
    return(b)

# Get a help an add function
help(add)

# Call the function add()
add(1)

# Call the function add()
add(2)

# Define a function for multiple two numbers
def Mult(a, b):
    c = a * b
    return(c)
    print('This is not printed')

result = Mult(12, 2)
print(result)

# Use mult() multiply two integers
print(Mult(2, 3))

# Use mult() multiply two floats
print(Mult(10.0, 3.14))

# Use mult() multiply two different type values together
print(Mult(2, "The BodyGuard "))

# Function Definition
def square(a):
    # Local variable b
    b = 1
    c = a * a + b
    print(a, "if you square + 1", c)
    return(c)

# Initializes Global variable
x = 3
# Makes function call and return function a y
y = square(x)
print(y)

# Directly enter a number as parameter
square(2)

# Define functions, one with return value None and other without return value
def MJ():
    print('The Bodyguard')
def MJ1():
    print('The Bodyguard')
    return(None)

# See the output
MJ()
MJ1()

# See what functions returns are
print(MJ())
print(MJ1())

# Define the function for combining strings
def con(a, b):
    return(a + b)

# Test on the con() function
print(con("This ", "is"))

# Block 1 : a and b calculation
a1 = 4
b1 = 5
c1 = a1 + b1 +  2 * a1 * b1 - 1
if(c1 < 0):
    c1 = 0
else:
    c1 = 5
print(c1)

# Block 2 : a and b calculation
a2 = 0
b2 = 0
c2 = a2 + b2 + 2 * a2 * b2 - 1
if(c2 < 0):
    c2 = 0
else:
    c2 = 5
print(c2)

# Make a function for the calculation above
def Equation(a, b):
    c = a + b + 2 * a * a - 1
    if(c < 0):
        c = 0
    else:
        c = 5
    return(c)

a1 = 3
b1 = 5
c1 = Equation(a1, b1)
print(c1)

a2 = 0
b2 = 0
c2 = Equation(a2, b2)
print(c2)

# Build-in function print()
album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5]
print(album_ratings)

# Use sum() to add every element in a list or tuple together
print(sum(album_ratings))

# Show the length of the list or tuple
print(len(album_ratings))

# Define a tuple
a = (1, 2)

# Pass the tuple to the sum function and store the result in a variable
c = sum(a)

# Print the result
print(f"The sum of the elements in the tuple {a} is {c}.")

# Define a list
a = [1, 2]

# Pass the list to the sum function and store the result in a variable
c = sum(a)

# Print the result
print(f"The sum of the elements in the list {a} is {c}.")

# Function example
def type_of_album(album, year_released):
    print(album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"

x = type_of_album("The Bodyguard", 1980)
print(x)

# Print the list using for loop
def PrintList(the_list):
    for element in the_list:
        print(element)

# Implement the print list function
PrintList(['1', 1, 'the man', "abc"])

# Compare Two Strings Directly using in operator
# add string
string = "The Bodyguard is the best album"
# Define a function
def check_string(text):
# Use if else statement and 'in' operatore to compare the string
    if text in string:
        return 'String matched'
    else:
        return 'String not matched'

print(check_string("The Bodyguard is the best"))

# Compare two strings using == operator and function
def compareStrings(x, y):
# Use if else statement to compare x and y
    if x == y:
        return 1

# Declare two different variables as string1 and string2 and pass string in it
string1 = "The BodyGuard is the best album"
string2 = "The BodyGuard is the best album"

# Declare a variable to store result after comparing both the strings
check = compareStrings(string1, string2)

# Use if else statement to compare the string
if check == 1:
    print("\nString Matched")
else:
    print("\nString Not Matched")

# Python Program to COunt words in a String using Dictionary
def freq(string):
    # Step 1: A list variable is declared and initialized to an empty list.
    words = []
    # Step 2: Break the string into list of words
    words = string.split() # or stirng.lower.split()
    # Step 3: Declare a dictionary
    Dict = {}
    # Step 4: Use for loop to iterate words and values to the dictionary
    for key in words:
        Dict[key] = words.count(key)
    # Step 5: Print the dictionary
    print("The Frequency of words is: ", Dict)

# Step 6: Call function and pass string in it
freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go")

# Example for setting param with default value
def isGoodRating(rating=4):
    if(rating < 7):
        print("this album sucks it's rating is", rating)
    else:
        print("this album is good its rating is", rating)

# Test the value with default value and with input
isGoodRating()
isGoodRating(10)

# Example of global variable
album = "The BodyGuard"
def printer1(album):
    internal_var1 = "Thriller"
    print(album, "is an album")

printer1(album)
# printer1(internal_var1)

album = "The Bodyguard"
def printer(album):
    global internal_var
    internal_var = "Thriller"
    print(album, "is an album")

printer(album)
printer(internal_var)

# Example of global variable
myFavouriteBand = "AC/DC"
def getBandRating(bandname):
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is: ", getBandRating("AC/DC"))
print("Deep Purple's rating is: ", getBandRating("Deep Purple"))
print("My favourite band is: ", myFavouriteBand)

# Deleting the variable "myFavouriteBand" from the previous example to demonstrate an example of a local variable
del myFavouriteBand
# Example of local variable
def getBandRating(bandname):
    myFavouriteBand = "AC/DC"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is: ", getBandRating("AC/DC"))
print("Deep Purple's rating is: ", getBandRating("Deep Purple"))
# print("My favourite band is", myFavouriteBand) = EROARE

# Example of global variable and local variable with the same name
myFavouriteBand = "AC/DC"
def getBandRating(bandname):
    myFavouriteBand = "Deep Purple"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:",getBandRating("AC/DC"))
print("Deep Purple's rating is: ",getBandRating("Deep Purple"))
print("My favourite band is:",myFavouriteBand)

# Collection and Function
def printAll(*args): # All the arguments are 'packed' into args which can be treated like a tuple
    print("No of arguments: ", len(args))
    for argument in args:
        print(argument)
#printAll with 3 arguments
printAll('Horsefeather', 'Adonis', 'Bone')
#printAll with 4 arguments
printAll('Sidecar', 'Long Island', 'Mudslide', 'Carriage')

def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada', Province='Ontario', City='Toronto')

def addItems(list):
    list.append("Three")
    list.append("Four")

myList = ["One", "Two"]
addItems(myList)
print(myList)

def div(a, b):
    return (a/b)

def con(a, b):
    return(a + b)

print(con(5, 6))

print(con(['a', 1], ['b', 1]))

# Python Program to Count words in a String using Dictionary
def freq(string,passedkey):

    #step1: A list variable is declared and initialized to an empty list.
    words = []

    #step2: Break the string into list of words
    words = string.split() # or string.lower().split()

    #step3: Declare a dictionary
    Dict = {}

    #step4: Use for loop to iterate words and values to the dictionary
    for key in words:
        if(key == passedkey):
            Dict[key] = words.count(key)
    #step5: Print the dictionary
    print("Total Count:",Dict)

#step6: Call function and pass string in it
freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go","little")