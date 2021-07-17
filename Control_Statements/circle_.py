
import turtle
from random import choice

pen = turtle.Pen()
turtle.bgcolor("black")

color = ['red', 'blue', '#123455', '#abcdef', 'green', 'yellow', '#123456', '#abc123', '#123abc']
rad = 150
#pen.speed(0.04)

for i in range(5):
    c = choice(color)
    pen.color('white', c)  # (fg, bg)
    pen.begin_fill()
    pen.circle(rad)
    pen.end_fill()
    pen.up()  # pen will be up and move without drawing
    pen.left(90)
    pen.forward(20)
    pen.right(90)
    pen.down()
    rad -= 20

turtle.exitonclick()
