# difference between the largest and smallest numbers.

#f(7,4,9) returns 5
#f(2,12,8) returns 10

def f(number1, number2, number3):
    largest = max(number1, number2, number3)
    smallest = min(number1, number2, number3)
    
    return largest - smallest

print(f(7, 4, 9))
print(f(2, 12, 8))  