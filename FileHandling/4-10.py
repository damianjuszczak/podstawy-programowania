# Write a program that prints those
# products whose price is less than 60 and whose
# stock is less than 40.

with open('clothing.csv', 'r') as file:
    next(file) 
    
    for line in file:
        columns = line.strip().split(',')
        
        price = float(columns[5])
        stock = int(columns[6])
        
        if price < 60 and stock < 40:
            print(f'Product: {columns[1]}, Price: ${price}')