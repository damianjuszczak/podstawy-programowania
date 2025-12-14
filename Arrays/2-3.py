# total expenses for each category
# total expenses for each week
# total expenses for a month

# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

food = 0
transport = 0
utilities = 0
weekly = []
total = 0

# Calculates expenses
# Use loop statements
for week in monthly_expenses:
    food += week[0]
    transport += week[1]
    utilities += week[2]

    current_week = 0

    for expense in week:
        current_week += expense

    weekly.append(current_week)

    total += current_week

    
# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print(f'Food: {food}')
print(f'Transport: {transport}')
print(f'Utilities: {utilities}')
print(f'Week 1: {weekly[0]}')
print(f'Week 2: {weekly[1]}')
print(f'Week 3: {weekly[2]}')
print(f'Week 4: {weekly[3]}')
print('---------------')
print(f'TOTAL: {total}')