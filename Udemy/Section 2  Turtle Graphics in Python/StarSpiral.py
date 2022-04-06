import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
color=["red","orange","yellow","green","blue","purple","pink"]
turtle.bgcolor("black")
for x in range(10000):
    t.pencolor(color[x%7])
    t.forward(2*x)
    t.left(150)