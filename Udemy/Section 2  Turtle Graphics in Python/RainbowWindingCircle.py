import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
color=["red","orange","yellow","green","blue","purple","pink"]
for x in range(10000):
    t.pencolor(color[x%7])
    t.forward(.015*x)
    t.left(10)