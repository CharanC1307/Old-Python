import turtle
t = turtle.Pen()
t.speed(0)
t.pencolor("blue")
for x in range(10000):
    t.forward(2*x)
    t.left(90)