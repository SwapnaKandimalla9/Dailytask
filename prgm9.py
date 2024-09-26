def is_armstrong_number(number):
    # Convert the number to a string to easily access digits
    str_num = str(number)
    num_digits = len(str_num)
    
    # Calculate the sum of the digits raised to the power of num_digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in str_num)
    
    # Check if the sum is equal to the original number
    return armstrong_sum == number

# Take input from the user
try:
    user_input = input("Enter a number: ")
    number = int(user_input)

    # Check if the number is an Armstrong number
    if is_armstrong_number(number):
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")

except ValueError:
    print("Please enter a valid integer.")
