def sum_of_digits(number):
    # Convert the number to a string to iterate over each digit
    return sum(int(digit) for digit in str(number))

# Take input from the user
user_input = input("Enter a number: ")

try:
    # Convert input to an integer
    number = int(user_input)
    # Get the sum of the digits
    result = sum_of_digits(number)
    # Print the result
    print(f"The sum of the digits of {number} is: {result}")
except ValueError:
    print("Please enter a valid number.")