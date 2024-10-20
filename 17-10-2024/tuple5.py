from collections import Counter

# Create a tuple
my_tuple = (1, 2, 3, 2, 4, 5, 1, 2, 3)

# Count the frequency of each element in the tuple
element_counts = Counter(my_tuple)

# Find the most common element and its count
most_common_element, most_common_count = element_counts.most_common(1)[0]
print( most_common_element)
print( most_common_count)
