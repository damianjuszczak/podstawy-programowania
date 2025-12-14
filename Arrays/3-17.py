# program that counts the number of occurrences of any value from a tuple.

# Tuple: 50,20,40,50,30,50
# Value: 50
# Number of occurrences: 3

t = (50, 20, 40, 50, 30, 50)

counter = 0
value = int(input('Enter number to find in touple: '))


for item in t:
    if item == value:
        counter += 1

        
