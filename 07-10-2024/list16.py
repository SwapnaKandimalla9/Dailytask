# Create a nested list of students and their grades
students = [
    ["Alice", 85],
    ["Bob", 92],
    ["John", 78],
    ["Sara", 90],
    ["Tom", 88]
]

# Print each student's name along with their grade
print("Student Grades:")
for student in students:
    name = student[0]  # Get the student's name
    grade = student[1]  # Get the student's grade
    print(f"{name}: {grade}")
