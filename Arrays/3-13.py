# occurs(number, array) that returns True if a given number is present in an array.
# program that checks whether the number entered from the keyboard
# is present in the array [15, 38, 7, 23, 14].

def occurs(number, array):
    return number in array

arr = [15, 38, 7, 23, 14]

user_input = int(input('Number: '))
in_array = occurs(user_input, arr)

if in_array == True:
    # print(f'Number: {user_input}')
    print(f'Array: {arr}')
    print(f'Result: number {user_input} appears in the array ')
else:
    print(f"Result: number {user_input} missing in the array")
    