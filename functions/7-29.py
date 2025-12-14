# function calculates the factorial recursively.
# factorial = silnia
def factorial(n):

# 0! = 1, 1! = 1
    if n==0 or n==1:
        return 1

# n! = n * (n-1)!
    if n > 1:
        return n * factorial(n-1)

number = 5
result = factorial(number)

print(f'The factorial of {number} is: {result}')


