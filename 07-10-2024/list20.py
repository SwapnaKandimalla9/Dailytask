# Given list of tuples (name, age)
students = [
    ("Alice", 25),
    ("Bob", 22),
    ("John", 30),
    ("Sara", 20),
    ("Tom", 28)
]

# Sort the list by age in ascending order
sorted_students = sorted(students, key=lambda x: x[1])

# Print the sorted list
print("Sorted list by age (ascending):")
for student in sorted_students:
    print(student)
