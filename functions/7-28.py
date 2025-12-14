#returns a number specifying the number of dice rolled the most times in a row

def f(dice):
    streak = 0
    streak_digit = None
    
    current = 0
    previous = None
    
    for digit in dice:
        if digit == previous:
            current += 1
        else:
            current = 1
            
        if current > streak:
            streak = current
            streak_digit = digit
            
        previous = digit
        
    return int(streak_digit)

print(f'f("5233165554211") returns {f("5233165554211")}')
print(f'f("2133")          returns {f("2133")}')