# Prices of 10 products in the computer store (in currency units)
product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]

# Number of units available for each product
product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]


def inventory_value(prices, quantities):
    total_value = 0
    
    item_quantity = len(prices)
    
    for i in range(item_quantity):
        price = prices[i]
        quantity = quantities[i]
        
        total_value += price * quantity
        
    return total_value


total_stock_value = inventory_value(product_prices, product_quantities)

print(f'Value of all goods: {total_stock_value:.2f}')