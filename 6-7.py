#age sort

#Child: under 13
#Teen: 13 to 19
#Adult: 20 to 64
#Senior: 65 or older

age = int(input('Enter your age e.g. "10": '))

if age < 13:
    print('Child under 13')
elif age <= 19:
    print('Teen: 13 to 19')
elif age <= 64:
    print('Adult: 20 to 64')
elif age <= 65:
    print('Senior: 65 or older')


