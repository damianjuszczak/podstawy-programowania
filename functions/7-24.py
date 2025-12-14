#An expression contains operators for adding and subtracting single-digit numbers.
# 
# f("2+3") returns 5
#f("3+8+1") returns 12
#f("2+3-4+5-0") returns 6


def f(expression):
# subtraction is just adding a negative number
    content = expression.replace('-', '+-').split('+')

    total = 0

    for i in content:
        number = int(i)  
        total += number
    
    return total

print(f('2+3'))          
print(f('3+8+1'))
print(f('2+3-4+5-0'))