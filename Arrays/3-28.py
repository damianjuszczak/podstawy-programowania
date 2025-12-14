# A two-dimensional array contains the following numbers:
# Create a program that calculates the sum of values in the last column.

def last_column_sum():
    matrix = [
        [7, 3, 7, 9, 0],
        [2, 9, 0, 1, 5],
        [3, 8, 6, 4, 7],
        [8, 7, 1, 1, 5]
    ]

    sum = 0

    for row in matrix:
        sum += row[-1]

    print(f'Sum of the last column: {sum}')

last_column_sum()