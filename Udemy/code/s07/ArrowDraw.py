# ArrowDraw.py
import random
import turtle
t = turtle.Pen()
t.speed(0)
t.turtlesize(2,2,2)
def up():
    t.forward(50)
def left():
    t.left(90)
def right():
    t.right(90)

wn = turtle.Screen()
#turtle.onscreenclick(draw_kaleido)
#wn.onscreenclick(draw_kaleido)


wn.onkeypress(up, "Up")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
turtle.listen()
turtle.done()
