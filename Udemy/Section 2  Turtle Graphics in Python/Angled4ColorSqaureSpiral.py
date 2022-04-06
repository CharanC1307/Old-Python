import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
color=["red","yellow","green","blue"]
for x in range(10000):
    t.pencolor(color[x%4])
    t.forward(2*x)
    t.left(91)