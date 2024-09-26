# Function to print the multiplication table
def multiplication_table(number):
    print(f"Multiplication Table for {number}:\n")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Take input from the user
try:
    user_input = input("Enter a number: ")
    number = int(user_input)

    # Print the multiplication table
    multiplication_table(number)

except ValueError:
    print("Please enter a valid integer.")

