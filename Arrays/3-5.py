# An array contains values: 15, 8, 31, 47, 2, 19
# program that calculates and prints the array and the arithmetic mean of array values
# Use the “for” loop statement.

arr = [15, 8, 31, 47, 2, 19]

total = 0

for i in arr:
    total += i

mean = total / len(arr)

print(f'Array: {arr}')
print(f'Arithmetic mean of array values: {mean:.2f}')