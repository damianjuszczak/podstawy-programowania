#price online

current_price = 140.00
previous_price = 200.00

print(f'Current product price: {current_price:.2f}')
print(f'Previous product price: {previous_price:.2f}')

price_difference = previous_price - current_price

percentage_decrease = (price_difference / previous_price) * 100

if percentage_decrease >= 10:
    print('Buy the product!!')
    print(f'Product price decreased by: {round(percentage_decrease)}%')
else:
    print('No purchase recommendation. Price reduction is less than 10%.')