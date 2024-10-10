import random

# Generate a list of 10 random integers
numbers = [random.randint(1, 100) for _ in range(10)]

# Print the original list
print("Original list:", numbers)

# Sort the list in descending order
numbers.sort(reverse=True)

# Print the sorted list
print("Sorted list in descending order:", numbers)
