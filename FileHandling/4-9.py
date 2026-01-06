import csv

file_path = 'it_company.csv'

print('GRAPHIC DESIGNERS')
print('=================')

with open(file_path, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
    
    for row in reader:   
        if row[2] == 'Graphic Designer':
            first_name = row[1]
            last_name = row[0]
            email = row[3]
            
            print(f'{first_name} {last_name},{email}')