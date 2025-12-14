#the area of ​​a triangle
#Heron's formula
#3, 4, 5 (result is 6)
#5, 12, 13 (result is 30)
#7, 24, 25 (result is 84)


###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math
def triangle_area(a,b,c):
    s = (a + b + c) / 2

    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area



# case 1
a1, b1, c1 = 3, 4, 5
triangle1 = triangle_area(a1, b1, c1)
print(f'The area of a triangle with sides {a1}, {b1}, {c1} is {triangle1}')

# case 2
a2, b2, c2 = 5, 12, 13
triangle2 = triangle_area(a2, b2, c2)
print(f'The area of a triangle with sides {a2}, {b2}, {c2} is {triangle2}')

# case 3
a3, b3, c3 = 7, 24, 25
triangle3 = triangle_area(a3, b3, c3)
print(f'The area of a triangle with sides {a3}, {b3}, {c3} is {triangle3}')
