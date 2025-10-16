"""Simple example: adds two numbers and prints the result."""

def add(number1, number2):
    """Return the sum of the two numbers provided as arguments."""
    return number1 + number2


def main():
    """Main function: initializes values, calls the add function, and displays the result."""
    num1 = 4
    num2 = 5
    total = add(num1, num2)
    print(f"The sum of {num1} and {num2} is {total}")


if __name__ == "__main__":
    main()

# pylint filename.py FOR RUN
