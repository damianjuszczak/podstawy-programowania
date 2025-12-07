#the payment card is secured with a four-digit PIN code (0805).
#checks if the PIN code entered in the payment terminal is correct. 
#the user has up to three possibilities for entering a PIN code.

correct_pin = '0805'

for i in range(3):
    pin = input('Enter the PIN code: ')

    if pin == correct_pin:
        print('Correct PIN')
        break
    
    print('Incorrect')

    if i == 2:
        print('Sorry, your payment card has been blocked.')


    