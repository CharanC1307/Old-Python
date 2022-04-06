import turtle
t = turtle.Pen()
t.speed(0)
for x in range(10000):
    t.forward(.015*x)
    t.left(10)