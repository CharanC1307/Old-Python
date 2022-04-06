import turtle
import winsound
import time
import os
from pygame import mixer
from tkinter import messagebox


class Game(turtle.Turtle):
    def __init__(self, color, startx, starty):
        turtle.Turtle.__init__(self)
        self.state="play"
        self.running=True
        self.run=True
        self.speed(0)
        self.color(color)
        self.penup()
        self.setposition(startx, starty)
        self.hideturtle()
    def write_word(self, align, what, how_much):
        self.align=align
        self.what=what
        how_much=how_much
        self.string=self.what+":" + str(how_much)
        self.write(self.string, False, align=self.align, font=("Arial", 11, "normal"))
    def rewrite(self, how_much):
        self.clear()
        self.string=self.what+":" + str(how_much)
        self.write(self.string, False, align=self.align, font=("Arial", 11, "normal"))

class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, setx, sety):
        turtle.Turtle.__init__(self, shape=spriteshape)
        self.penup()
        self.speed(0)
        self.setposition(setx, sety)
        self.setheading(90)

class Player(Sprite):
    def __init__(self, spriteshape, startx, starty):
        Sprite.__init__(self, spriteshape, startx, starty)
        self.speed=15
    def move(self, left_or_right, state):
        if state=="play":
            x=self.xcor()
            if left_or_right=="left":
                x=x-self.speed
                if x<-265:
                    x=-265
            elif left_or_right=="right":
                x=x+self.speed
                if x>265:
                    x=265
            self.setx(x)

class Bullet(Sprite):
    def __init__(self, spriteshape, startx, starty):
        Sprite.__init__(self, spriteshape, startx, starty)
        self.speed=1.5
        self.state="ready"
    def fire_bullet(self, character, file):
        if self.state=="ready":
            winsound.PlaySound(file, winsound.SND_ASYNC)
            self.state="fire"
            self.setposition(character.xcor(), character.ycor()+10)
            self.showturtle()
    def lower_speed_of_bullet(self, write_method):
        self.speed=round(self.speed-.1, 2)
        if self.speed<0:
            self.speed=0
        write_method(self.speed)
    def raise_speed_of_bullet(self, write_method):
        self.speed=self.speed+.1
        self.speed=round(self.speed,2)
        if self.speed>3:
            self.speed=3
        write_method(self.speed)
    def move(self, speed):
        if self.state=="fire":
            self.sety(self.ycor()+speed)
        if self.ycor()>275:
            self.state="ready"
            self.setposition(-1000, 1000)

class Enemies(Sprite):
    def __init__(self, spriteshape, spriteshape2, setx, sety):
        Sprite.__init__(self, spriteshape, setx, sety)
        self.setheading(90)
        self.frame=0
        self.frames=[spriteshape, spriteshape2]
    def animate(self):
        self.frame=self.frame+1
        if self.frame>=len(self.frames):
            self.frame=0
        self.shape(self.frames[self.frame])
        turtle.ontimer(self.animate, 500)