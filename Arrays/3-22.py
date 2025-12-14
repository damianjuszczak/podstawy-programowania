# function rand_elem(array) that returns a randomly selected array element.
import random

def rand_elem(array):
    l = len(array)

    random_item = random.randint(0, l - 1)

    return array[random_item]

arr = [7,9,2,4,5,6]

print(rand_elem(arr))
print(rand_elem(arr))
print(rand_elem(arr))
print(rand_elem(arr))
print(rand_elem(arr))
