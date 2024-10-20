#display the common elements
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
common_elements = set1 & set2
if common_elements:
    print("Common elements using & operator:", common_elements)
else:
    print("No common elements using & operator.")
