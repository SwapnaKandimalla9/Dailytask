# Initialize a list with some numbers
numbers = [1, 2, 3, 4, 5]

# Print the original list
print("Original list:", numbers)

# Add a new element to the list
numbers.append(6)
print("List after adding 6:", numbers)

# Remove an element from the list (for example, removing the number 3)
numbers.remove(3)
print("List after removing 3:", numbers)

# Extend the list with another list of numbers
additional_numbers = [7, 8, 9, 10]
numbers.extend(additional_numbers)
print("List after extending with additional numbers:", numbers)
