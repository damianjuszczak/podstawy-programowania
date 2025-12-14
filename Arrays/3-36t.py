def matrix_2d_to_1d(matrix):

    result = []

    for row in matrix:
        
        for item in row:
            
            result.append(item)

    return result


arr_1 = [
    [2, 3],
    [1, 5]
]

arr_2 = [
    [5, 0, 3, 7, 5],
    [9, 0, 9, 1, 2]
]

arr_3 = [
    [2, 1],
    [3, 5],
    [7, 4],
    [2, 6]
]

print(f'2d: {arr_1}')
print(f'1d: {matrix_2d_to_1d(arr_1)}')
print()

print(f'2d: {arr_2}')
print(f'1d: {matrix_2d_to_1d(arr_2)}')
print()

print(f'2d: {arr_3}')
print(f'1d: {matrix_2d_to_1d(arr_3)}')