
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Update set1 to keep only elements that are in set1 and not in set2
set1.difference_update(set2)
print("Updated set1 (using difference_update):", set1)
