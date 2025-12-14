import converters

# Test existing functions
meters = 1.5
print(f'{meters} meters is {converters.m_to_cm(meters)} cm')

cm = 250
print(f'{cm} cm is {converters.cm_to_m(cm)} meters')

# Centimeters to Inches
cm_val = 50.8
inches_result = converters.cm_to_inches(cm_val)
print(f'{cm_val} cm is {inches_result} inches')

# Feet and Inches to Centimeters
feet = 6
inches = 1
cm_result = converters.feet_inches_to_cm(feet, inches)
print(f'{feet} feet and {inches} inches is {cm_result} cm')