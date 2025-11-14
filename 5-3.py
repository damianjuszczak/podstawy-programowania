###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
cuboid_surface_area = 2 * (a * b + b * c + a * c)
cuboid_volume= a * b * c

print(f'When {a, b, c = } cuboid volume is {cuboid_volume} \nand cuboid surface area equals {cuboid_surface_area}')