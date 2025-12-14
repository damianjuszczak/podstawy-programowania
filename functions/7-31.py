#Define a function power(x, n) that calculates xn. Apply recursion. Then, calculate 5,3.

#Tip: xn = x * xn-1

def power(x, n):
    if n == 0:
        return 1
    
    return x * power(x, n - 1)

result = power(5, 3)
print(f'power(5, 3) returns {result}')