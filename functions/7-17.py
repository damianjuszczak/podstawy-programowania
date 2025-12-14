#palindrome 

#f("radar') returns True
#f("12-11-21") returns True
#f("book") returns False

def f(palindrome):
    return palindrome == (palindrome)[::-1]

print(f('radar'))
print(f('12-11-21'))
print(f('book'))