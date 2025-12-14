def min_max(matrix):
    min_value = matrix[0][0]
    min_row = 0
    min_column = 0
    
    max_value = matrix[0][0]
    max_row = 0
    max_column = 0
    
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            value = matrix[row][column]
            
            if value < min_value:
                min_value = value
                min_row = row
                min_column = column
            
            if value > max_value:
                max_value = value
                max_row = row
                max_column = column
                
    print(f'Smallest valueue: {min_value} row: {min_row}, column: {min_column}')
    print(f'Largest valueue: {max_value}, row: {max_row}, column: {max_column}')

arr = [
    [-38, 19], 
    [5, 40], 
    [-7, 11], 
    [29, 16]
]

min_max(arr)