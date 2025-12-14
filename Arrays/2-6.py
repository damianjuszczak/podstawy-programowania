# [
#    [0,0,0],
#    [0,0,0],
#    [0,0,0]
# ]

# modify to: 

# 1 0 0
# 0 1 0
# 0 0 1

# use loop statement

matrix = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]

for i in range(len(matrix)):
    matrix[i][i] = 1

for row in matrix:
    print(row[0], row[1], row[2])