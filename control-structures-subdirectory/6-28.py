#20 fibonacci numbers

x=1
y=2

print('first 20 fibonacci numbers: ', end = ' ')

for i in range(20):
    print(x, end = ' ')

    next = x + y
    x = y
    y = next

    