# Two numbers and an operator are given.
# returns the result of an arithmetic operation
#f(2,3, "+") returns 5
#f(2,3, "%") returns 2
#f(2,3, "**") returns 8
#f(2,3, "*") returns 6
#f(2,3, "-") returns -1

def f(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '%':
        return number1 % number2
    elif operator == '**':
        return number1 ** number2
    else:
        return "Invalid Operator"

print(f"f(2,3, '+') returns {f(2, 3, '+')}")
print(f"f(2,3, '%') returns {f(2, 3, '%')}")
print(f"f(2,3, '**') returns {f(2, 3, '**')}")
print(f"f(2,3, '*') returns {f(2, 3, '*')}")
print(f"f(2,3, '-') returns {f(2, 3, '-')}")