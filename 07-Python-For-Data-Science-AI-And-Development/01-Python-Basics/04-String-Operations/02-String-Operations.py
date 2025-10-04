# Use quotation marks for defining string
print("The BodyGuard")

# Use single quotation marks for defining string
print('The BodyGuard')

# Digitals and spaces in string
print('1 2 3 4 5 6')

# Special characters in string
print('@#2_#&*^%$')

# Print the string
print("Hello!")

# Assign string to variable
name = "The BodyGuard"
print(name)

# Print the first element in the string
print(name[0])

# Print the element on index 6 in the string
print(name[6])

# Print the element on the 10th index in the string
print(name[10])

# Print the last element in the string
print(name[-1])

# Print the first element in the string
print(name[-13])

# Find the length of string
len("The BodyGuard")

# Take the slice on variable name with only index 0 to index 3
print(name[0:4])

# Take the slic eon variable name with only index 8 to index 11
print(name[8:12])

# Get every second element, starting with the index 0. The elements on index 0, 2, 4 ...
print(name[::2])

# Get every second element in the range from index 0 to index 4
print(name[0:5:2])

# Concatenate two strings
statement = name + " is the best album"
print(statement)

# Print the string for 3 times
print(3 * "The BodyGuard ")

# Concatenate strings
name = "The BodyGuard"
name = name + " is the best album"
print(name)

# New line escape sequence
print("The BodyGuard\n is the best album")

# Tab escape sequence
print("The BodyGuard \t is the best album")

# Include back slash in string
print("The BodyGuard \\ is the best album")

# r will tell python that string will be display as raw string
print(r"The BodyGuard \ is the best album")

# Convert all the characters in string to upper case
a = "Thriller is the sixth studio album"
print("Before upper: ", a)
b = a.upper()
print("After upper: ", b)

# Replace the old substring with the new target substring is the segment has been found in the string
a = "The BodyGuard is the best album"
b = a.replace('BodyGuard', 'Janet')
print(b)

# Find the substring in the string. Only the index of the first element of substring in string will be the output
name = "The BodyGuard"
print(name.find('he'))

# Find the substring in the string
print(name.find('Guard'))

# If cannot find the substring in the string
print(name.find('Jasdfasdasdf'))

# Split the substring into list
name = "The BodyGuard"
split_string = (name.split())
print(split_string)

import re

s1 = "The BodyGuard is the best album"

# Define the pattern to search for
pattern = r"Body"

# Use the search() function to search for the pattern in the string
result = re.search(pattern, s1)

# Check if a match was found
if result:
    print("Match found!")
else:
    print("Match not found!")

pattern = r"\d\d\d\d\d\d\d\d\d\d"  # Matches any ten consecutive digits
text = "My Phone number is 1234567890"
match = re.search(pattern, text)

if match:
    print("Phone number found: ", match.group())
else:
    print("No Match")

pattern = r"\W" # Matches any non-word character
text = "Hello, world!"
matches = re.findall(pattern, text)
print("Matches: ", matches)

s2 = "The BodyGuard is the best album of 'Whitney Houston'."

# Use the findall() function to find all occurrences of the "st" in the string
result = re.findall("st", s2)

# Print out the list of matched words
print(result)

# Use the split function to split the string bt the "\s"
split_array = re.split(r"\s", s2)

# The split_array contains all the substrings, split by whitespace characters
print(split_array)

# Define the regular expression pattern to search for
pattern = r"Whitney Houston"

# Define the replacemenet string
replacement = "legend"

# Use the sub function to replace the pattern with the replacement string
new_string = re.sub(pattern, replacement, s2, flags=re.IGNORECASE)

# The new string contains the original string with the pattern replaced by the replacement string
print(new_string)

# EXERCISES
a = "1"
b = "2"
c = a + b
print(a)
print(b)
print(c)
d = "ABCDEFG"
print(d[0:3])
e = 'clocrkr1e1c1t'
print(e[::2])
print(r"\\")
f = "You are wrong"
print(f.upper())
f2="YOU ARE RIGHT"
print(f2.lower())
g = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"
print(g.find("snow"))
g.replace("Mary", "Bob")
print(g)
g.replace(',', '.')
print(g)
g.split()
print(g)

s3 = "House number- 1105"
result = re.search(r"\d", s3)

# Check if a match was found
if result:
    print("Digit found")
else:
    print("Digit not found.")

str1= "The quick brown fox jumps over the lazy dog."
# Use re.sub() to replace "fox" with "bear"
new_str1 = re.sub(r"fox", "bear", str1)
print(new_str1)

str2 = "How much wood would a woodchuck chuck, if a woodchuck could chuck wood?"
# Use re.findall() to find all occurrences of "woo"
matches = re.findall(r"woo", str2)
print(matches)
print("Python is \"awesome\"")
