import csv

try:
    with open('it_company.csv', 'r') as file:
        reader = csv.reader(file)
        line_counter = 0
        
        for row in reader:
            print(', '.join(row))
            line_counter += 1
            
            if line_counter == 5:
                input('Press Enter key...')
                line_counter = 0

except FileNotFoundError:
    print('File not found')

