#f('1082') returns True
#f('2035') returns True
#f('1114') returns False
#f('7071') returns False

def f(product_code):
    
    if len(product_code) != 4:
        return False
    
    digit_sum = int(product_code[0]) + int(product_code[1]) + int(product_code[2])
    control_digit = int(product_code[3])
    
    remainder = digit_sum % 7
    
    return remainder == control_digit

print(f('1082'))
print(f('2035'))
print(f('1114'))
print(f('7071'))