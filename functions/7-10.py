# number of negative even numbers in the range 
#f(-7,8) returns 3
#f(-1,11) returns 0

def f(x, y):
    counter = 0
    for i in range(x, y + 1):
        if i < 0 and i & 2 == 0:
            counter += 1
    return counter 

print(f'f(-7,8) returns {f(-7, 8)}')
print(f'f(-1,11) returns {f(-1, 11)}')



