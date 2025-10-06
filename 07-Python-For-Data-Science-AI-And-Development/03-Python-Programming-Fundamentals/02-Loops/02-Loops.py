# Use the range
print(range(3))

# For loop example
dates = [1982, 1980, 1973]
N = len(dates)

for i in range(N):
    print(dates[i])

# Example of for loop
for i in range(0, 8):
    print(i)

# Example of for loop, loop through list
for year in dates:
    print(year)

# Use for loop to change the elements in list
squares = ['red', 'yellow', 'green', 'purple', 'blue']
for i in range(0, 5):
    print("Before square: ", i, ' is ', squares[i])
    squares[i] = 'white'
    print("After square ", i, ' is ', squares[i])

# Loop through the list and iterate on both index and element value
squares = ['red', 'yellow', 'green', 'purple', 'blue']
for i, square in enumerate(squares):
    print(i, square)

# While loop Example
dates = [1982, 1980, 1973, 2000]
i = 0
year = dates[0]
while(year != 1973):
    print(year)
    i = i + 1
    year = dates[i]

print("It took ", i, "repetitions to get out of loop.")

for i in range(-5, 6):
    print(i)

Genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for Genre in Genres:
    print(Genre)

squares = ['red', 'yellow', 'green', 'purple', 'blue']
for square in squares:
    print(square)

PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
Rating = PlayListRatings[0]
while (i < len(PlayListRatings) and Rating >= 6):
    print(Rating)
    i = i + 1  # This prints the value 10 only once
    Rating = PlayListRatings[i]
    i = i + 1  # Try uncommenting the line and comment the previous i = i + 1, and see the difference, 10 value will get printed twice because when the loop starts it will print Rating and then with PlayListRatings[0], it will again assign the value 10 to Ratings.

squares = ['orange', 'orange', 'purple', 'blue', 'orange']
new_squares = []
i = 0
while(i < len(squares) and squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1
print(new_squares)
