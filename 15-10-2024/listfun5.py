def list_to_single_integer(lst):
    # Convert the list of integers to a single string
    single_integer_str = ''.join(str(num) for num in lst)
    # Convert the string back to an integer
    return int(single_integer_str)
integer_list = [1, 2, 3, 4, 5]
result = list_to_single_integer(integer_list)
print(result)  
