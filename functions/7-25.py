#sum of numbers in the range
#f(1,20) returns 24
#f(10,30) returns 48

def f(x, y):
    total = 0
    for num in range(x, y + 1):
        if num % 2 == 0 and num % 3 == 0 and num % 4 != 0:
            total += num
    return total

print(f(1, 20))
print(f(10, 30))  