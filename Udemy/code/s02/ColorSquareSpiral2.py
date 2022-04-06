import turtle
t=turtle.Pen()
t.speed(0)
turtle.bgcolor('black')
colors=['red', 'yellow', 'blue', 'green']
for x in range(200):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(91)