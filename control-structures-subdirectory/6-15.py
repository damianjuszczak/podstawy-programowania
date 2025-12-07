#EAN13

'''Enter EAN-13 article number: 5901230094938
Article number is correct
Article manufactured in Poland'''

# lenght == 13

ean = input('Enter ean (13 digit number): ')
correct = False



if len(ean) == 13:
    correct = True
    print('Number is correct')

    if ean[0:3] == '590':
      print('Product was manufactured in Poland')
        




