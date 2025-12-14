# Define a function compare(array1, array2)

# Array1: water book sky
# Array2: water book sky
# Comparison: arrays are the same

# 1. ["water","book","sky"]   ["water","book","sky"]
# 1. [True,False]   [True,False,True]
# 1. [5,3,1]   [5,3,1]
# 1. [3,2,1]   [3,2]

def compare(array1, array2):
    if len(array1) != len(array2):
        return False
    
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
        
    return 'arrays are the same'

array1_a = ["water","book","sky"]
array1_b = ["water","book","sky"]
result1 = compare(array1_a, array1_b)
print(f'Array1: {array1_a}\nArray2: {array1_b}\nComparison: {result1}')

array2_a = [True,False]
array2_b = [True,False,True]
result2 = compare(array2_a, array2_b)
print(f'Array1: {array2_a}\nArray2: {array2_b}\nComparison: {result2}')

array3_a = [5,3,1]
array3_b = [5,3,1]
result3 = compare(array3_a, array3_b)
print(f'Array1: {array3_a}\nArray2: {array3_b}\nComparison: {result3}')

array4_a = [3,2,1]
array4_b = [3,2]
result4 = compare(array4_a, array4_b)
print(f'Array1: {array4_a}\nArray2: {array4_b}\nComparison: {result4}')



