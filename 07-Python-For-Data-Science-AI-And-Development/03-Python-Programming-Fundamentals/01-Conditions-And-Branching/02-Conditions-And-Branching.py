# Condition Equal
a = 5
print(a == 6)

# Greater than Sign
i = 6
print(i > 5)

# Greater than Sign
i = 2
print(i > 5)

# Inequality Sign
i = 2
print(i != 6)

# Inequality Sign
i = 6
i != 6

# Use Equality sign to compare the strings
print("ACDC" == "The Bodyguard")

# Use Inequality sign to compare the strings
print("ACDC" != "The Bodyguard")

# Compare characters
print('B' > 'A')

# Compare characters
print('BA' > 'AB')

# If statement example
age = 19
# age = 18

# Expression that can be true or false
if age > 18:
    # Within an indent, we have the expression that is run if the condition is true
    print("you can enter")
# The statements after if statement will run regardless if the condition is true or false
print("move on")

# Else statement example
age = 18
# age = 19
if age > 18:
    print("you can enter")
else:
    print("go see Meat Loaf")
print("move on")

# Elif statement example
age = 18
if age > 18:
    print("you can enter")
elif age == 18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf")
print("move on")

# Condition statement example
album_year = 1983
#album_year = 1970
if album_year > 1980:
    print("Album year is greater than 1980")
print("do something")

# Condition statement example
album_year = 1983
#album_year = 1970
if album_year > 1980:
    print("Album year is greater than 1980")
else:
    print("less than 1980")
print("do something...")

# Condition statement example
album_year = 1980
if (album_year > 1979) and (album_year < 1990):
    print("Album year was in between 1980 and 1989")
print("")
print("Do Stuff...")

# Condition statement example
album_year = 1990
if (album_year < 1980) or (album_year > 1989):
    print("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's")

# Condtion statement example
album_year = 1983
if not (album_year == 1984):
    print("Album year is not 1984")

player_name = "Lionel Messi"
sport = "Soccer"
achievements = 7

if achievements > 10:
    print(f"{player_name} plays {sport} and has {achievements} achievements.")
else:
    print(f"{player_name} does not have more than 10 achievements.")


player_name = "Roger Federer"
sport = "Tennis"
achievements = 20

if sport == "Tennis" or achievements == 20:
    print(f"{player_name} meets the criteria! They play {sport} and have {achievements} achievements.")
else:
    print(f"{player_name} does not meet the criteria.")

player_name = "Usain Bolt"
sport = "Athletics"
achievements = 8

if achievements < 10 and sport != "Soccer":
    print(f"{player_name} plays {sport} and has only {achievements} achievements.")
else:
    print(f"{player_name} does not meet the criteria.")