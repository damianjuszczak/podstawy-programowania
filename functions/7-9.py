#  sum of the digits of a number.
# when true -> even
# when false -> odd
# f(3124,True) returns 6
# f(3124,False) returns 4
# f(20576,False) returns 12
# f(20576,True) returns 8
# f(13115,True) returns 0

def f(number, even):
    sum_total = 0
    
    for char in str(number):
        digit = int(char)
        digit_even = (digit % 2 == 0)
        
        if digit_even == even:
            sum_total += digit
            
    return sum_total

print(f'f(3124, True) returns: {f(3124, True)}')
print(f'f(3124, False) returns: {f(3124, False)}')
print(f'f(20576, False) returns: {f(20576, False)}')
print(f'f(20576, True) returns: {f(20576, True)}')
print(f'f(13115, True) returns: {f(13115, True)}')