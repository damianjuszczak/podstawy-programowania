# Create a program that prints all unique elements in an array. Sample result:
# Array: 2 3 2 5 8 1 9 8
# Unique elements: 3 5 1 9

arr = [2, 3, 2, 5, 8, 1, 9, 8]

def unique(arr):
    return set(arr)

print(f'Array: {arr}')
print(f'Unique elements: {unique(arr)}')