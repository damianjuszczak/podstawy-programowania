
#program that checks what number was entered from
#the keyboard and prints one of the messages

number = int(input('Enter number: '))

if number > 0 :
    print(f'Number {number} is positive')
elif number == 0 :
    print(f'Number {number  } is 0')
elif number < 0 :
    print(f'Number {number} is negative')


