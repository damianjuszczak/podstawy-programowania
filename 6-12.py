"""Number of products purchased: 5
Product price: 40
Amount to pay: 170.00"""

# 25% discount for ea product over two

product_price = 40
amount = 5
final_price = 0
discount = 0.75

if amount <= 2:
    final_price = amount * product_price
else:
    final_price = ((product_price) * 2 ) + ((product_price * discount) * (amount - 2))

print(f'Number of produckts purchased: {amount}')
print(f'Product price: {product_price}')
print(f'Amount to pay: {final_price}')