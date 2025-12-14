def transpose_matrix(m):
    rows = len(m)
    cols = len(m[0])

    matrix_t = []
    for item in range(cols):
        matrix_t.append([0] * rows)

    for i in range(rows):
        for j in range(cols):
            matrix_t[j][i] = m[i][j]

    return matrix_t


matrix_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
]

matrix_3 = [
    [5, 6, 7, 8]
]


matrices = [matrix_1, matrix_2, matrix_3]

for m in matrices:
    print('---- o ----')
    for row in m:
        for item in row:
            print(f'{item}', end=' ')
        print()

    transposed = transpose_matrix(m)

    print('---- t ----')
    for row in transposed:
        for item in row:
            print(f'{item}', end=' ')
        print()
    print() 