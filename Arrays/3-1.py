# array contains integer numbers: 34,7,19,4,21,8
# program that calculates and prints the number of even values in the array
# Use the ‘while’ loop statement.

arr = [34, 7, 19, 4, 21, 8]

counter = 0
i = 0

while i < len(arr):
    if arr[i] % 2 == 0:
        counter += 1
    i += 1

print('Even number in arr:', counter)
