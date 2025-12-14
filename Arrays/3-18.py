# A function that returns the second largest element in an array
# A function that returns the difference between the largest and smallest values in an array
# A function that returns the median of numbers in an array.

# Do not use built-in functions. The median is the middle value in the ordered sequence of numbers:

# A function that returns a two-element array containing the smallest and largest values in an array

# A function that returns array elements as a string, separated by the minus sign

# Then, write a program that for the sequence of numbers:

# 7,3,8,5,2
# calculates and prints results. Sample result:

# Numbers: 7,3,8,5,2
# Second largest number: 7 
# Median: 5
# Smallest and largest number: 2,8
# Numbers as a string: 7-3-8-5-2

import MyArrays

sequence = [7, 3, 8, 5, 2]

numbers_formatted = ''
for i in range(len(sequence)):
    numbers_formatted += str(sequence[i])
    if i < len(sequence) - 1:
        numbers_formatted += ','
print(f'Numbers: {numbers_formatted}')

second_max = MyArrays.second_largest(sequence)
print(f'Second largest number: {second_max}')

median_value = MyArrays.median(sequence)
if median_value == int(median_value):
    print(f'Median: {int(median_value)}')
else:
    print(f'Median: {median_value}')

min_max = MyArrays.min_max(sequence)
print(f'Smallest and largest number: {min_max[0]},{min_max[1]}')

number_str = MyArrays.array_to_string(sequence)
print(f'Numbers as a string: {number_str}')