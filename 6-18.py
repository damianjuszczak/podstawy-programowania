# plane coordinates
x = 5
y = 2

print(f'x = {x}')
print(f'y = {y}')

if x == 0:
    print(f'y axis')
elif y == 0:
    print(f'z axis')
elif x == 0 and y == 0:
    print('position 0,0')
elif x > 0 and y > 0:
    print(f'P({x},{y}) -> 1st quadrant')
elif x < 0 and y > 0:
    print(f'P({x},{y}) -> 2nd quadrant')
elif x < 0 and y < 0:
    print(f'P({x},{y}) -> 3rd quadrant')
elif x > 0 and y < 0:
    print(f'P({x},{y}) -> 4th quadrant')
