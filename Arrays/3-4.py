# array contains arr: -15, 8, -31, 47, -2, 19
# program that finds and prints the maximum and minimum number
# Do not use available functions

arr = [-15, 8, -31, 47, -2, 19]

max_value = arr[0]
min_value = arr[0]

for i in arr:
    if i > max_value:
        max_value = i
    
    if i < min_value:
        min_value = i

print('Max number:', max_value)
print('Min number:', min_value)