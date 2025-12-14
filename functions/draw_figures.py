import turtle

window = turtle.Screen()
window.bgcolor("black")

pen = turtle.Turtle()
pen.speed(15)

def draw_square(length):
    for i in range(4):
        pen.forward(length)
        pen.right(90)

draw_square(100)

pen.hideturtle()
window.mainloop() # last statement in turtle