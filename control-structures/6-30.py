#lottery coupon
x = 7
y = 7
grid = x * y

for row in range(1, x + 1):
    line = ''
    for col in range(1, y + 1):
 # Calculate the number for the current position 
        position = row + (col - 1) * x

        line += f'{position:<2} '


    print(line)