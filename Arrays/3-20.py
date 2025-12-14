#  program to separate even and odd itembers of a given array of integers.
# Put all even itembers first, and then odd itembers.

def even_odd():
    arr = [7, 9, 2, 4, 5, 6]
    
    evens = []
    odds = []
    
    for item in arr:
        if item % 2 == 0:
            evens.append(item)
        else:
            odds.append(item)
            
    result = evens + odds
    
    print(f'arr = {arr}')
    print(f'arr = {result}')


even_odd()