"""
Enter price: 24.72
Enter discount %: 15
Price with discount: 21.01
Reduction: 3.71 
"""
price = float(input("Enter price: "))
discount = float(input("Enter discount %: "))
price_with_discount = price * ((100 - discount) * .01 )
reduction = price - price_with_discount

print(f"Entered price: {price:.2f}")
print(f"Discount amount: {discount:.0f}%")
print(f"Price with discount: {price_with_discount:.2f}")
print(f"Reduction: {reduction:.2f}")