# def sort_copy(arr):
 
#     sorted_arr = []
#     for item in arr:
#         sorted_arr.append(item)
    
#     n = len(sorted_arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if sorted_arr[j] > sorted_arr[j + 1]:
#                 sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
#     return sorted_arr

def second_largest(arr):
    if len(arr) < 2:
        return None
    if arr[0] > arr[1]:
        largest = arr[0]
        second = arr[1]
    else:
        largest = arr[1]
        second = arr[0]

    for i in range(2, len(arr)):
        num = arr[i]
        if num > largest:
            second = largest
            largest = num
        elif num > second:
            second = num
            
    return second

def range_diff(arr):
    if not arr:
        return 0
    smallest = arr[0]
    largest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return largest - smallest

def median(arr):
    sorted_arr = arr[:] 
    n = len(sorted_arr)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
    
    mid_index = n // 2
    
    if n % 2 == 1:
        return sorted_arr[mid_index]
    else:
        return (sorted_arr[mid_index - 1] + sorted_arr[mid_index]) / 2

def min_max(arr):
    if not arr:
        return []
    smallest = arr[0]
    largest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return [smallest, largest]

def array_to_string(arr):
    result_str = ''
    for i in range(len(arr)):
        result_str += str(arr[i])
        if i < len(arr) - 1:
            result_str += '-'
    return result_str