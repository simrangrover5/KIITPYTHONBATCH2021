
import turtle

pen = turtle.Pen()
pen.color("red", "blue")  # (fg, bg)
#pen.begin_fill()
rad = 50
for i in range(7):
    pen.circle(rad)
    rad += 20
#pen.end_fill()

turtle.exitonclick()
