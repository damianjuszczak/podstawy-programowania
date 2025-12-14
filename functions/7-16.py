# fibonacci 
#f(5) returns 3
#f(9) returns 21

def f(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    return f(n - 1) + f(n - 2)

print(f'f(5) returns {f(5)}')
print(f'f(9) returns {f(9)}')