# Create a list of numbers
original_list = [1, 2, 3, 4, 5]

# Assign the list to another variable
assigned_list = original_list

# Modify the original list
original_list.append(6)

# Check if the assigned list also changes
print("Original list after modification:", original_list)
print("Assigned list after original modification:", assigned_list)

# Create a copy of the original list
copied_list = original_list.copy()

# Modify the copy
copied_list.append(7)

# Show that modifying the copy does not affect the original list
print("Original list after modifying the copy:", original_list)
print("Copied list after modification:", copied_list)
