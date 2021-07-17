
import turtle 
from random import choice

turtle.bgcolor('black')
color = ['coral', 'red', 'white', 'blue', '#123456', '#abcdef']
pen = turtle.Pen()
pen.speed(0)

for i in range(300):
    pen.pencolor(choice(color))
    pen.forward(i)
    pen.left(201)
    
turtle.exitonclick()
