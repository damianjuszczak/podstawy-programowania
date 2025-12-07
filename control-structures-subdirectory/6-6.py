# parking meter

time = int(input("Enter number of hours of parking: "))
price1 = 5
price2 = 15
price3 = 20
final_price = 0

if time <= 2:
    final_price = price1
elif time <=6:
    final_price = price2
else:
    final_price = price3

print(f'Car was parked for: {time}h\nAmount to pay: {final_price}')