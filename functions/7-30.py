#for the given natural number n calculates the sum of all natural numbers between 1 and n.
#Apply recursion.
# Then, create a program that calculates the sum of natural numbers in the range <1,10>.

def sum_natural(n):
    if n <= 1:
        return n
    else:
        return n + sum_natural(n - 1)

n = 10
result = sum_natural(n)

print(f"The sum of natural numbers from 1 to {n} is: {result}")