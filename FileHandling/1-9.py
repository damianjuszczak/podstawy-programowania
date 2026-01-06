###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.csv'

# Position
job_title = 'Software Engineer'

with open(file_name, 'r') as file:
    next(file)
    
    counter = 1
    
    for line in file:
        if job_title in line:
            print(f'{counter}. {line.strip()}')
        counter += 1