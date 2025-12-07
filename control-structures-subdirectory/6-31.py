#Write a program that prints 20 integer random numbers in the range of 5 to 10.

import random

#range (x,y)
x = 5
y = 10

#20 random numbers in range
for i in range(20):
    rng = random.randint(x,y)

    print(f'{rng}', end=' ')