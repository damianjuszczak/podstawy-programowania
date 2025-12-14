#f("101101") returns True
#f("1311a10100") returns False

def f(binary_number):
    # Check if string are a subset of '0' and '1'
    return set(binary_number) <= {'0', '1'}

print(f("101101"))
print(f("1311a10100"))