#program to merge two dicts
# Create two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Method 1: Using update() method
merged_dict1 = dict1.copy()  # Create a copy to preserve the original
merged_dict1.update(dict2)
print("Merged dictionary using update():", merged_dict1)

