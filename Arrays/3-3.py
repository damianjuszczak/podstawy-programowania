# Create a program that computes the second power of each array element.
# Array: 8 2 5 1 9
# 2nd power: 64 4 25 1 81

import math

arr = [8, 2, 5, 1, 9]
arr_second_power = []
i = 0

for i in range(len(arr)):
    i = int((math.pow(arr[i], 2)))
    arr_second_power.append(i)


print(arr_second_power)