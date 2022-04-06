# ClickArrowDraw.py
import turtle
t = turtle.Pen()
t.speed(0)
t.turtlesize(2,2,2)
turtle.bgcolor("blue")
t.pencolor("green")
def up():
    t.forward(50)
def left():
    t.left(45)
def right():
    t.right(45)
def move(x,y):
    t.penup()
    t.setpos(x,y)
    t.pendown()
def thicker():
    t.width( t.width() + 2 )
def thinner():
    t.width( t.width() - 2 )
    
turtle.onkeypress(up, "Up")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")
turtle.onkeypress(thicker, ">")
turtle.onkeypress(thinner, "<")
turtle.listen()
turtle.onscreenclick(move)

turtle.mainloop()

