# program that checks whether the first array is a subset of the second one 

def subset(arr1, arr2):
    for item in arr1:
        found = False
        
        for target in arr2:
            if item == target:
                found = True
                break
        
        if not found:
            return False
            
    return True


arr_a = [7, 9, 2, 4, 5, 6]
arr_b = [1, 2, 3, 4, 5, 6]
arr_c = [2, 3]

if subset(arr_a, arr_b):
    print('It is a subset')
else:
    print('Not a subset')

if subset(arr_c, arr_b):
    print('It is a subset')
else:
    print('Not a subset')