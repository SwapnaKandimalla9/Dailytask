# Create a list of strings
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Print the original list
print("Original list:", fruits)

# Reverse the list using the reverse() method
fruits_reversed_method = fruits.copy()  # Create a copy to preserve the original lists
fruits_reversed_method.reverse()
print("List after reverse() method:", fruits_reversed_method)

# Reverse the list using slicing
fruits_reversed_slicing = fruits[::-1]
print("List after slicing [::-1]:", fruits_reversed_slicing)

# Compare the results
if fruits_reversed_method == fruits_reversed_slicing:
    print("Both methods yield the same result.")
else:
    print("The methods yield different results.")
