# subtract one from the first element of the array
# increase the last array element by 4
# multiple the middle array element by 2

#An array contains values: 1, 2, 3, 4, 5. 

arr = [1, 2, 3, 4, 5]
print(f'Array: {arr}')

arr[0] = arr[0] - 1
print(f'Array: {arr}')

arr[-1] = arr[-1] + 4
print(f'Array: {arr}')

arr[2] = arr[2] * 2
print(f'Array: {arr}')