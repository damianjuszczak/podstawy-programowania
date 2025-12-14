#  program that, for the given array of real arr, prints the number of elements that are greater than the given

def greater():
    arr = [10.5, -3.5, 8.0, 5.5, 2.0, -9.5, 12.0, -1.5]

    print(f'Array: {arr}')

    compare = float(input('Value to compare: '))

    count = 0
    for item in arr:
        if item > compare:
            count += 1

    print(f'Number of elements greater than {compare}: {count}')

if __name__ == '__main__':
    greater()