# program that prints the longest name

arr = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']

longest = arr[0]
max_length = len(arr[0])

for i in arr:
    current = len(arr)

    if current > max_length:
        max_length = current
        longest = i

names = ' '.join(arr)

print('Names:', names)
print('Longest name:', longest)


