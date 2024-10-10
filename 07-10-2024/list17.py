# Create a list of numbers from 1 to 20
numbers = list(range(1, 21))

# Generate separate lists for even and odd numbers
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

# Print the results
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
