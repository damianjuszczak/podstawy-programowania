
###
# Draw a square
#
def draw_square(pen, length):
    for i in range(4):
        pen.forward(length)
        pen.right(90)

def draw_triangle(pen, length):
    # isosceles triangle 
    for i in range(3):
        pen.forward(length)
        pen.left(120)

def draw_rectangle(pen, length_a, length_b):
    for i in range(2):
        pen.forward(length_a)
        pen.right(90)
        pen.forward(length_b)
        pen.right(90)