#NiceHexSpiral_Alex2.py
import turtle   
colors=['red', 'purple', 'blue',
        'green', 'yellow', 'orange']
t=turtle.Pen()
t.speed(0)
turtle.bgcolor('black')
for x in range(200):
    t.pencolor(colors[x%6])
    t.width(x/50+1)
    t.circle(x)        
    t.left(59)
