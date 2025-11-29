n = int(input('Enter the amount of primes to find: '))

count = 0
number = 2

#check if n is prime
while count < n:
    is_prime = True
    
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(number, end=' ')
        count += 1
        
    number += 1