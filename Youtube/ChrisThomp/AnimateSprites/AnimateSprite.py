import turtle
import time

wn=turtle.Screen()
wn.title("Animate Sprite")
wn.bgcolor("black")


wn.register_shape("C:\Brothers\Charan\Python\MyProjects\Youtube\ChrisThomp\AnimateSprites\Pictures\invader1.gif")
wn.register_shape("C:\Brothers\Charan\Python\MyProjects\Youtube\ChrisThomp\AnimateSprites\Pictures\invader2.gif")

class Enemy(turtle.Turtle):
    def __init__(self, shape1, shape2):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape(shape1)
        self.setheading(90)
        self.frame=0
        self.frames=[shape1, shape2]


    def animate(self):
        self.frame=self.frame+1
        if self.frame>=len(self.frames):
            self.frame=0
        self.shape(self.frames[self.frame])
        wn.ontimer(self.animate, 500)

enemy=Enemy("C:\Brothers\Charan\Python\MyProjects\Youtube\ChrisThomp\AnimateSprites\Pictures\invader1.gif", "C:\Brothers\Charan\Python\MyProjects\Youtube\ChrisThomp\AnimateSprites\Pictures\invader2.gif")
enemy.animate()

while True:
    wn.update()


wn.mainloop()