#Amount  : 15.84
#VAT 23% :  3.64

amount = float(input('Write amount before 23% VAT applied: '))
vat = amount * .23

print(f'Amount before 23% VAT applied: {amount:.2f} \nAmount after 23% VAT applied: {vat:.2f} ')