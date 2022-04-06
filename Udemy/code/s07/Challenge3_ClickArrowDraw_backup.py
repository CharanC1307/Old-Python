# ArrowDraw.py
import turtle
t = turtle.Pen()
t.speed(0)
t.turtlesize(2,2,2)
def up():
    t.forward(50)
def left():
    t.left(45)
def right():
    t.right(45)
def bigger():
    t.width(t.width() + 2)
def smaller():
    t.width(t.width() - 2)
def move(x,y):
    t.penup()
    t.setpos(x,y)
    t.pendown()
turtle.onkeypress(up, "Up")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")
turtle.onkeypress(bigger, ">")
turtle.onkeypress(smaller, "<")
turtle.listen()
turtle.onscreenclick(move)

