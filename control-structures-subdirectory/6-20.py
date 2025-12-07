#program that converts a decimal number into a binary number.


#read a decimal number from the keyboard.
number_decimal = int(input('Enter decimal number: '))
#empty string
number_binary = ''

#store number for print
number = number_decimal

#when input is 0
if number_decimal == 0:
    number_binary = '0'

#divide the number by 2 and note the remainder.
while number_decimal > 0:
    remainder = number_decimal % 2
    
#converting int remainder to string
    number_binary = str(remainder) + number_binary
#floor division
    number_decimal = number_decimal // 2


print(f'{number}(10) = {number_binary}(2)')
