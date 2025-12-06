###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# Determine temperature in degree Celsius
# Calculate temperature in Kelvin
# Calculate temperature in Fahrenheit
# Print results

temperature_celsius = float(input('Enter temperature in Celsius: '))
temperature_kelvin = temperature_celsius + 273.15
temperature_fahrenheit = (temperature_celsius * 1.8) + 32

print(f'Temperature in Celsius: {temperature_celsius}')
print(f'Temperature in Kelvin: {temperature_kelvin}')
print(f'Temperature in Fahrenheit: {temperature_fahrenheit}')