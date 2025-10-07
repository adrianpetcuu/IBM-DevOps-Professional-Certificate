# 1 / 0

# y = a + 5

# a = [1, 2, 3]
# print(a[10])

# potential code before try catch
# try:
    # code to try to execute
# except:
    # code to execute if there is an exception

# code that will still execute if there is an exception

a = 1
try:
    b = int(input("Please enter a number to divide a = "))
    a = a / b
    print("Success a = ", a)
except:
    print("There was an error")

# potential code before try catch

# try:
# code to try to execute
# except (ZeroDivisionError, NameError):
# code to execute if there is an exception of the given types

# code that will execute if there is no exception or a one that we are handling

# potential code before try catch

# try:
# code to try to execute
# except ZeroDivisionError:
# code to execute if there is a ZeroDivisionError
# except NameError:
# code to execute if there is a NameError

# code that will execute if there is no exception or a one that we are handling

# potential code before try catch

# try:
# code to try to execute
# except ZeroDivisionError:
# code to execute if there is a ZeroDivisionError
# except NameError:
# code to execute if there is a NameError
# except:
# code to execute if ther is any exception

# code that will execute if there is no exception or a one that we are handling

a = 1
try:
    b = int(input("Please enter a number to divide a"))
    a = a / b
    print("Success a = ", a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")

# potential code before try catch

# try:
# code to try to execute
# except ZeroDivisionError:
# code to execute if there is a ZeroDivisionError
# except NameError:
# code to execute if there is a NameError
# except:
# code to execute if ther is any exception
# else:
# code to execute if there is no exception

# code that will execute if there is no exception or a one that we are handling

# potential code before try catch

# try:
# code to try to execute
# except ZeroDivisionError:
# code to execute if there is a ZeroDivisionError
# except NameError:
# code to execute if there is a NameError
# except:
# code to execute if ther is any exception
# else:
# code to execute if there is no exception
# finally:
# code to execute at the end of the try except no matter what

# code that will execute if there is no exception or a one that we are handling

a = 1
try:
    b = int(input("Please enter a number to divide a"))
    a = a / b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a = ", a)

a = 1
try:
    b = int(input("Please enter a number to divide a"))
    a = a / b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a = ", a)
finally:
    print("Processing Complete")

# PRACTICE EXERCISES

def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
# Test case
numerator = int(input("Enter the numerator value:- "))
denominator = int(input("Enter the denominator value:- "))
print(safe_divide(numerator, denominator))

import math

def perform_calculation(number1):
    try:
        result = math.sqrt(number1)
        print(f"Result: {result}")
    except ValueError:
        print("Error: Invalid input! Please enter a positive integer or a float value.")
# Test case
number1 = float(input("Enter the number:- "))
perform_calculation(number1)


def complex_calculation(num):
    try:
        result = num / (num - 5)
        print(f"Result: {result}")
    except Exception as e:
        print("An error occurred during calculation.")
# Test case
user_input = float(input("Enter a number: "))
complex_calculation(user_input)