import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
color="red"
for x in range(10000):
    turtle.bgcolor(color[x])
    t.forward(2*x)
    t.left(90)