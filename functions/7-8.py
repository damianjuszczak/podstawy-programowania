def f(amount_to_pay):
    if amount_to_pay <= 0:
        return 0
    
    coins = [5, 2, 1]
    coins_total = 0
    
    for coin in coins:
        count = amount_to_pay // coin 
        coins_total += count
        amount_to_pay %= coin
        
    return coins_total

print(f'f(23) returns {f(23)}')
print(f'f(8)  returns {f(8)}')
print(f'f(2)  returns {f(2)}')
print(f'f(0)  returns {f(0)}')