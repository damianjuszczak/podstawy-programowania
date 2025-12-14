#f('5290312400019022') returns '52**********9022'

import card_security

def main():

    credit_card = '5290312400019022'
    hidden = card_security.hide(credit_card)
    
    print(f'Original: {credit_card}')
    print(f'Masked:   {hidden}')

if __name__ == '__main__':
    main()