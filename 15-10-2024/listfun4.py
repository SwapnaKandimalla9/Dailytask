def remove_column(nested_list, col_index):
    # Check if the column index is valid
    if not nested_list or col_index < 0 or col_index >= len(nested_list[0]):
        print("Invalid column index.")
        return nested_list

    # Remove the specified column
    for row in nested_list:
        del row[col_index]

    return nested_list
nested_list = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]s
]

column_to_remove = 2
updated_list = remove_column(nested_list, column_to_remove)
print(updated_list)
