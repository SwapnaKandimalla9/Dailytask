#program to find the largest of three numbers using is statements
def find_largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Take input from the user
try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    number3 = float(input("Enter the third number: "))

    # Find the largest number
    largest = find_largest(number1, number2, number3)

    # Print the result
    print(f"The largest number among {number1}, {number2}, and {number3} is: {largest}")

except ValueError:
    print("Please enter valid numbers.")
