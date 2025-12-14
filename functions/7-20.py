# n-prime

#f(1) returns 2
#f(5) returns 11

import math

def prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def f(n):
    count = 0
    result = 1 
    
    while count < n:
        result += 1
        if prime(result):
            count += 1
            
    return result

print(f(1))
print(f(5))