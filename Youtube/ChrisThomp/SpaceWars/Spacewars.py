import turtle
import os
import random
import math
import winsound

os.system("cls")


turtle.tracer(1)
turtle.setundobuffer(1)
turtle.hideturtle()


wn=turtle.Screen()
wn.title("Space Wars")
wn.bgcolor("black")
wn.setup(width=700, height=700)


class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape=spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.setposition(startx, starty)
        self.speed=1
    def move(self):
        self.forward(self.speed)
        if self.xcor()>290:
            self.setx(290)
            self.right(60)
        if self.xcor()<-290:
            self.setx(-290)
            self.right(60)
        if self.ycor()>290:
            self.sety(290)
            self.right(60)
        if self.ycor()<-290:
            self.sety(-290)
            self.right(60)
    def is_collision(self, other):
        if (self.xcor() >= (other.xcor() - 20)) and \
        (self.xcor() <= (other.xcor() + 20)) and \
        (self.ycor() >= (other.ycor() - 20)) and \
        (self.ycor() <= (other.ycor() + 20)):
            return True
        else:
            return False
        """distance=(math.sqrt(((self.xcor()-other.xcor())**2)+((self.ycor()-other.ycor())**2)))
        if distance<15:
            return True
        else:
            return False"""

class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed=4
        self.lives=3
    def turn_left(self):
        self.left(45)
    def turn_Right(self):
        self.right(45)
    def accelerate(self):
        self.speed=self.speed+1
    def deaccelerate(self):
        self.speed=self.speed-1

class Enemy(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed=6
        self.setheading(random.randint(0,360))

class Ally(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed=8
        self.setheading(random.randint(0,360))
    def move(self):
        self.forward(self.speed)
        if self.xcor()>290:
            self.setx(290)
            self.left(60)
        if self.xcor()<-290:
            self.setx(-290)
            self.left(60)
        if self.ycor()>290:
            self.sety(290)
            self.left(60)
        if self.ycor()<-290:
            self.sety(-290)
            self.left(60)

class Bullet(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed=20
        self.status="ready"
        self.shapesize(stretch_wid=.3, stretch_len=.5, outline=None)
        self.goto(-1000, 1000)
    def fire(self):
        if self.status=="ready":
            play_sound("C:\Brothers\Charan\Python\MyProjects\Youtube\ChrisThomp\SpaceWars\laser.wav")
            x=player.xcor()
            y=player.ycor()
            self.goto(x, y)
            heading=player.heading()
            self.setheading(heading)
            self.status="firing"
    def move(self):
        if self.status=="ready":
            self.goto(-1000, 1000)
        if self.status=="firing":
            self.forward(self.speed)
        if self.xcor()>290 or self.xcor()<-290 or self.ycor()>290 or self.ycor()<-290:
            self.goto(-1000, 1000)
            self.status="ready"

class Game():
    def __init__(self):
        self.level=1
        self.score=0
        self.state="playing"
        self.lives=3
        self.wn=turtle.Screen()
        self.wn.title("Space Wars")
        self.wn.bgcolor("black")
        self.wn.setup(width=700, height=700)
    def border(self):
        self.pen=turtle.Turtle()
        self.pen.pensize(3)
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.penup()
        self.pen.setposition(-300,-300)
        self.pen.pendown()
        for i in range(4):
            self.pen.forward(600)
            self.pen.left(90)
        self.pen.penup()
    def show_status(self):
        self.pen.undo()
        score=self.score
        msg="Score:"+str(score)
        self.pen.penup()
        self.pen.goto(-300, 310)
        self.pen.write(msg, font=("Times", 16, "normal"))


def play_sound(sound_file, time=0):
    winsound.PlaySound(sound_file, winsound.SND_ASYNC)
    if time>0:
        t=int(time*1000)
        turtle.ontimer(lambda: play_sound(sound_file, time), t)


player=Player("triangle", "white", 0, 0)

enemy=Enemy("circle", "red", -100, 0)

ally=Ally("square", "blue", 0, 0)

bullet=Bullet("triangle", "yellow", 0, 0)

game=Game()
game.border()
game.show_status()


wn.listen()
"""wn.onkeypress(player.turn_left, "Left")
wn.onkeypress(player.turn_Right, "Right")
wn.onkeypress(player.accelerate, "Up")
wn.onkeypress(player.deaccelerate, "Down")"""
wn.onkey(player.turn_left, "Left")
wn.onkey(player.turn_Right, "Right")
wn.onkey(player.accelerate, "Up")
wn.onkey(player.deaccelerate, "Down")
wn.onkey(bullet.fire, "space")


while True:
    wn.update()
    player.move()
    enemy.move()
    ally.move()
    bullet.move()
    if player.is_collision(enemy):
        play_sound("C:\Brothers\Charan\Python\MyProjects\Youtube\ChrisThomp\SpaceWars\explosion.wav")
        x=random.randint(-250, 250)
        y=random.randint(-250, 250)
        enemy.goto(x,y)
        game.score=game.score-10
        game.show_status()
    """if player.is_collision(ally):
        x=random.randint(-250, 250)
        y=random.randint(-250, 250)
        ally.goto(x,y)"""
    if bullet.is_collision(enemy):
        x=random.randint(-250, 250)
        y=random.randint(-250, 250)
        enemy.goto(x,y)
        bullet.status="ready"
        game.score=game.score+10
        game.show_status()
    if bullet.is_collision(ally):
        x=random.randint(-250, 250)
        y=random.randint(-250, 250)
        ally.goto(x,y)
        bullet.status="ready"
        game.score=game.score-5
        game.show_status()


turtle.mainloop()