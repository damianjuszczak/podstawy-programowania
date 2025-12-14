# Write a program that calculates which expense category was the most expensive.

categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

def most_expensive(category_list, expense_list):
    max_cost = max(expenses)
    index = expense_list.index(max_cost)

    return category_list[index], max_cost

top_category, top_cost = most_expensive(categories, expenses)

print(f'The most expensive category is: {top_category} : {top_cost}')