def identity_matrix(n):
    matrix = []
    
    for r in range(n):
        row = []
        
        for c in range(n):
            if r == c:
                row.append(1)
            else:
                row.append(0)
        
        matrix.append(row)
        
    return matrix

def print_matrix(matrix):
    for row in matrix:
        for val in row:
            print(val, end=' ')
        print()
    print()

dimensions = [3, 5, 8]

for n in dimensions:
    print(f'size {n}:')
    m = identity_matrix(n)
    print_matrix(m)