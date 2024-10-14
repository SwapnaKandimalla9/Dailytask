# Create a list of numbers
original_list = [1, 2, 3, 4, 5]

# Create an alias by assigning the original list to another variable
alias_list = original_list

# Modify the original list
original_list.append(6)

# Show that both lists reflect the change
print("Original list after modification:", original_list)
print("Alias list after original modification:", alias_list)

# Create a cloned list using the copy() method
cloned_list = original_list.copy()

# Modify the cloned list
cloned_list.append(7)

# Show that modifying the cloned list does not affect the original list
print("Original list after modifying the cloned list:", original_list)
print("Cloned list after modification:", cloned_list)
