# Create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Display the original sets
print("Original set1:", set1)
print("Original set2:", set2)

# Update set1 to keep only items that are common to both sets
set1.intersection_update(set2)

# Display the updated set1
print("Updated set1 after removing non-common items:", set1)
