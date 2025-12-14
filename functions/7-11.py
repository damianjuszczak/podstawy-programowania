#  function which returns True if at least one of the numbers is negative or False otherwise
#f(11,6,-4) returns True
#f(5,4,14) returns False

def f(n1,n2,n3):
    return n1 < 0 or n2 < 0 or n3 < 0

print(f'f(11,6,-4) returns {f(11, 6, -4)}')
print(f'f(5,4,14) returns {f(5, 4, 14)}')



