#sum of numbers

#f(1027) returns 0
#f(230335) returns 9
#f(513553007) returns 21

def f(number):
    recurring = str(number)
    total = 0

    for digit in recurring:
        if recurring.count(digit) > 1:
            total += int(digit)

    return total

print(f(1027))
print(f(230335))
print(f(513553007))

