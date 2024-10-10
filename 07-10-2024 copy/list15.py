# Create a 3x3 matrix using a nested list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print the matrix
print("3x3 Matrix:")
for row in matrix:
    print(row)

# Access and print the element at row 2, column 3 (indices are 0-based)
row = 1  # Row 2
col = 2  # Column 3
element = matrix[row][col]
print(f"Element at row 2, column 3: {element}")

