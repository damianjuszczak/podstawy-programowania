'''The atm.py program simulates a simple ATM
where the user can deposit, withdraw, or check the balance. 
add two more functions to the program:
check pin and change pin'''

# ATM (cash machine) simulator

balance = 1000  # Initial balance
pin = '1111' # initial 4-digit PIN code
pin_correct = False

while True:
    entered_pin = input('Please enter your 4-digit PIN: ')
    
    if entered_pin == pin:
        print('\nPIN accepted. Welcome to the ATM!')
        break  
    else:
        print('Incorrect PIN.')
        exit()
    

while True:
    print('ATM Menu:')
    print('1. Check balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Change PIN')
    print('5. Exit')

    choice = input('Choose an option (1-4): ')

    if choice == '1':
        print(f'Your current balance is: €{balance}')
    elif choice == '2':
        amount = float(input('Enter the amount to deposit: '))
        balance += amount
        print(f'€{amount} has been deposited. New balance: €{balance}')
    elif choice == '3':
        amount = float(input('Enter the amount to withdraw: '))
        if amount <= balance:
            balance -= amount
            print(f'€{amount} has been withdrawn. New balance: €{balance}')
        else:
            print('Insufficient balance.')
    elif choice == '4':
            new_pin = input('Enter your new 4-digit PIN: ')
            if len(new_pin) == 4:
                    confirm_pin = input('Re-enter your new PIN to confirm: ')
                    
                    if new_pin == confirm_pin:
                        pin = new_pin  # Update the PIN
                        print('Your PIN has been successfully changed.')
                    else:
                        print('PINs do not match. Change failed.')
            else:
                    print('Invalid PIN format. PIN must be exactly 4 digits.')

    elif choice == '5':
        break  # Exit the loop
    else:
        print('Invalid option. Please try again.')

