'''Enter the amount in PLN: 18
The amount of PLN 18 in coins:
5 PLN coins: 3
2 PLN coins: 1
1 PLN coins: 1'''
#show number in polish coins as few as possible

amount = int(input('Enter amount in PLN: '))

coins_5 = amount // 5
amount = amount % 5
coins_2 = amount // 2
amount = amount % 2
coins_1 = amount


    

print(f'5PLN coins: {coins_5}')
print(f'2PLN coins: {coins_2}')
print(f'1PLN coins: {coins_1}')

