import turtle
import winsound
import time
import os
from pygame import mixer
from tkinter import messagebox


dirpath=(os.path.dirname(os.path.abspath(__file__)))
picpath=dirpath+"/Stuff/Pictures/"
musicpath=dirpath+"/Stuff/Music/"


wn=turtle.Screen()
wn.tracer(0)
wn.setup(700, 700)
wn.bgcolor("black")
wn.title("Space Invaders")
wn.register_shape(picpath+"invader1.gif")
wn.register_shape(picpath+"invader2.gif")
wn.register_shape(picpath+"spaceship.gif")
wn.bgpic(picpath+"space_invaders_background.gif")
wn.register_shape(picpath+"SpaceInvadersLaserDepiction.gif")


pen=turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()


class Sprite():
    def __init__(self, x, y, shape):
        self.state="active"
        self.shape=shape
        self.x=x
        self.y=y
    def update(self, width, height):
        if self.state=="active":
            if self.health<=0:
                self.reset()
        #self.da=0
    def border_check(self, width, height):
        if self.x>width/2-10:
            self.x=width/2-10
            self.dx=self.dx*-1
        elif self.x<-width/2+10:
            self.x=-width/2+10
            self.dx=self.dx*-1
        if self.y>height/2-10:
            self.y=height/2-10
            self.dy=self.dy*-1
        elif self.y<-height/2+10:
            self.y=-height/2+10
            self.dy=self.dy*-1
    def render(self, pen):
        if self.state=="active":
            pen.goto(self.x, self.y)
            pen.shape(self.shape)
            pen.stamp()

sprite=Sprite(0, 0, picpath+"spaceship.gif")
sprite.render(pen)

wn.mainloop()