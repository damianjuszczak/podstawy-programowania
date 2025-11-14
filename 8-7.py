# program that converts integer into binary and hexadecimal

number = int(input("Enter number integer number: "))
number_bin = bin(number)
number_hex = hex(number)

print(f'integer: {number}\nbinary: {number_bin}\nhexadecimal: {number_hex}')