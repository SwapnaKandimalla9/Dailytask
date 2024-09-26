# Function to count even and odd numbers in a list
def count_even_odd(numbers):
    even_count = 0
    odd_count = 0

    for number in numbers:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count

# Example list of numbers
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Count even and odd numbers
even_count, odd_count = count_even_odd(numbers_list)

# Print the results
print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")
