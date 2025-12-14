# Define a function that sorts an arr of numbers using the bubble sort algorithm. 

# Bubble sort

def buble_sort(arr):

    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr


car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
print(car_fuel_consumption)
sorted_car_fuel_consumption = buble_sort(car_fuel_consumption) 
print(sorted_car_fuel_consumption)


bank_transactions = [-150, -20, 300, -45, -60, 500, -120]
print(bank_transactions)
sorted_bank_transactions = buble_sort(bank_transactions)
print(sorted_bank_transactions)