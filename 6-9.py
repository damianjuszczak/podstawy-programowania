#polish female name

name = input('Enter name: ')

#check if ends with letter a
is_female_name = name.lower().endswith('a')

if is_female_name:
    print(f'{name} is Polish female name')