#program to remove duplicates from the list
def remove_duplicates(lst):
    return list(set(lst))

# Example usage
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(my_list)
print(unique_list) 
