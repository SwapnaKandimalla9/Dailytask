# Given list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Specific element to check
element_to_check = 5

# Check if the element exists in the list
if element_to_check in numbers:
    position = numbers.index(element_to_check)
    print(f"Element {element_to_check} found at position: {position}")
else:
    print("Element not found")
