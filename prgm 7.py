#program to calculate the factorial of a number using a for loop
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Take input from the user
user_input = input("Enter a non-negative integer: ")

try:
    # Convert input to an integer
    number = int(user_input)
    
    if number < 0:
        print("Please enter a non-negative integer.")
    else:
        # Calculate the factorial
        fact = factorial(number)
        # Print the result
        print(f"The factorial of {number} is: {fact}")

except ValueError:
    print("Please enter a valid integer.")
