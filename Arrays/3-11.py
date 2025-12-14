# program that sorts elements of an arrayay containing integer numbers.
# Define a function bubblesort(arrayay) 

def bubblesort(array):

    n = len(array)

    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    
    return array


array1 = [4, 36, 12, 28, 9, 44, 5]
array1_sorted = bubblesort(array1)
array2 = [5, 1, 36]
array2_sorted = bubblesort(array2)
array3 = [15, 8, 31, 47, 2, 19]
array3_sorted = bubblesort(array3)

print(array1)
print(f'Sorted: {array1_sorted}')
print()
print(array2)
print(f'Sorted: {array2_sorted}')
print()
print(array3)
print(f'Sorted: {array3_sorted}')
print()