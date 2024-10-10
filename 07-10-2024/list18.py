# Function to get unique elements from a list
def get_unique_elements(numbers):
    return list(set(numbers))

# Example list of integers (you can modify this list)
input_list = [1, 2, 2, 3, 4, 4, 5, 5, 6]

# Get the unique elements
unique_list = get_unique_elements(input_list)

# Print the results
print("Original list:", input_list)
print("Unique elements:", unique_list)
