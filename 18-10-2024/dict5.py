#program to combine two dicts
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
combined_dict = dict1.copy()  
for key, value in dict2.items():
    if key in combined_dict:
        combined_dict[key] += value  
    else:
        combined_dict[key] = value  
print( combined_dict)
