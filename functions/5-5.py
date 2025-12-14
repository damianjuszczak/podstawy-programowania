import turtle
import figures 

window = turtle.Screen()
window.bgcolor("black")

pen = turtle.Turtle()
pen.speed(15)
pen.color("white")

# first square
figures.draw_square(pen, 100)

pen.penup()
pen.goto(-250, 250)
pen.pendown()

# second square
figures.draw_square(pen, 50)

pen.penup()
pen.goto(-150, -100)
pen.pendown()

# first triangle
figures.draw_triangle(pen, 80)

pen.penup()
pen.goto(-50, -300)
pen.pendown()

# second triangle
figures.draw_triangle(pen, 80)

pen.penup()
pen.goto(100, 100)
pen.pendown()

# first rectangle
figures.draw_rectangle(pen, 120, 60)

pen.penup()
pen.goto(-200, -250)
pen.pendown()

# second rectangle
figures.draw_rectangle(pen, 80, 40)

pen.hideturtle()
window.mainloop() #last statement in tutrle graphics program