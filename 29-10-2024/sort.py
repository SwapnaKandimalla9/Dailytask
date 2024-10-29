def sort_dict_by_value(d):
    return sorted(d.items(), key=lambda item: item[1])

sample_dict = {'a': 3, 'b': 1, 'c': 2}
sorted_list = sort_dict_by_value(sample_dict)
print(sorted_list)  
