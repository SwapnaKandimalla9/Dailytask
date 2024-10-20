# Create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Display the original sets
print("Original set1:", set1)
print("Original set2:", set2)

# Find items in set2 that are not in set1
unique_items = set2.difference(set1)

# Update set1 with the unique items from set2
set1.update(unique_items)

# Display the updated set1
print("Updated set1 after adding unique items from set2:", set1)
