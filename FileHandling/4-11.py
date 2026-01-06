with open('powers.txt', 'w') as file:
    for n in range(1, 101):
        power_nd = n ** 2
        power_rd = n ** 3
        
        line = f'{n},{power_nd},{power_rd}'
        
        print(line)
        
        file.write(line + '\n')

print('\nSaved as powers.txt')