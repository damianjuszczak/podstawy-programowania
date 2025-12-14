# existed array: 15 8 31 47 2 19 
# reverse array: 19 2 47 31 8 15

arr = [15, 8, 31, 47, 2, 19]
arr_reversed = []

for i in range(len(arr)-1, -1, -1):
    arr_reversed.append(arr[i])

print(arr_reversed)