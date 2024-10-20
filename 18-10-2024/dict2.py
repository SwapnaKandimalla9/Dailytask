#program to check given balue is present in the dict or not
my_dict = {'a': 1, 'b': 2, 'c': 3}
value_to_check = 2

# Using 'in' with values()
if value_to_check in my_dict.values():
    print("The value is present in the dictionary.")
else:
    print("The value {value_to_check} is NOT present in the dictionary.")

