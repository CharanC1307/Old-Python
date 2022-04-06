import turtle
import os
import math
import random
import time
import platform
import winsound
import pygame
#Score is +1 every second you stay alive.
#Enemy have two live
#If you kill enemy you get 2 points
#Every wave enemy speed +.75 and enemies +3
#Every wave score +(wave number)10
#enemies get faster when they get closer
os.system("cls")

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.setup(width=700, height=700)
wn.bgpic("C:\Brothers\Charan\Python\Youtube\ChrisThomp\SpaceInvader\pictures\space_invaders_background.gif")

"""wn.delay(0)"""
wn.tracer(0)

wn.register_shape("C:\Brothers\Charan\Python\Youtube\ChrisThomp\SpaceInvader\pictures\invader.gif")
wn.register_shape("C:\Brothers\Charan\Python\Youtube\ChrisThomp\SpaceInvader\pictures\spaceship.gif")
wn.register_shape("C:\Brothers\Charan\Python\Youtube\ChrisThomp\SpaceInvader\pictures\SpaceInvadersLaserDepiction.gif")
wn.register_shape("C:\Brothers\Charan\Python\Youtube\ChrisThomp\AnimateSprites\Pictures\invader1.gif")
wn.register_shape("C:\Brothers\Charan\Python\Youtube\ChrisThomp\AnimateSprites\Pictures\invader2.gif")


pen=turtle.Turtle()
pen.pensize(3)
pen.hideturtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.setposition(-300,-300)
pen.pendown()
for i in range(4):
    pen.forward(600)
    pen.left(90)
pen.hideturtle()


gamescore=0

score=turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.setposition(-300, 330)
score.hideturtle()

scorestring="Score:" + str(gamescore)
score.write(scorestring, False, align="left", font=("Arial", 11, "normal"))

High_Score_In_Space_Invader = open('High_Score_In_Space_Invader', 'r')
high_score = High_Score_In_Space_Invader.read()
High_Score_In_Space_Invader.close()

wave=turtle.Turtle()
wave.speed(0)
wave.color("white")
wave.penup()
wave.setposition(-300, 315)
wave.hideturtle()

wavestring="High Score:" + high_score
wave.write(wavestring, False, align="left", font=("Arial", 11, "normal"))


s=1

bulletspeed=turtle.Turtle()
bulletspeed.speed(0)
bulletspeed.color("white")
bulletspeed.penup()
bulletspeed.setposition(-300, 300)
bulletspeed.hideturtle()

bulletspeedstring="Bullet Speed:" + str(s)
bulletspeed.write(bulletspeedstring, False, align="left", font=("Arial", 11, "normal"))


player=turtle.Turtle()
player.color("blue")
player.shape("C:\Brothers\Charan\Python\Youtube\ChrisThomp\SpaceInvader\pictures\spaceship.gif")
player.penup()
player.speed(0)
player.setposition(280, -250)
player.setheading(90)

playerspeed=15


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


number_of_enemies=30

enemies=[]

for i in range (number_of_enemies):
    e=Enemy("C:\Brothers\Charan\Python\Youtube\ChrisThomp\AnimateSprites\Pictures\invader1.gif", "C:\Brothers\Charan\Python\Youtube\ChrisThomp\AnimateSprites\Pictures\invader2.gif")
    enemies.append(e)

'''
z=0
x=-150
y=230
'''

enemy_start_x=-210
enemy_start_y=265
enemy_number=0

for enemy in enemies:
    enemy.animate()
    enemy.speed(0)
    x=enemy_start_x+(50*enemy_number)
    y=enemy_start_y
    enemy.setposition(x, y)
    enemy_number=enemy_number+1
    if enemy_number==10:
        enemy_number=0
        enemy_start_y=enemy_start_y-40
    '''x=random.randint(-200, 200)
    y=random.randint(100, 250)'''
    '''
    #This is my way to have rows of alieans
    enemy.setposition(x, y)
    enemy.setheading(90)
    if enemy.xcor()>100:
        z=0
        y=y-40
    else:
        z=z+50
    x=-150+z'''

enemy_life=2

a=.15
enemyspeed=a


bullet=turtle.Turtle()
bullet.color("yellow")
bullet.shape("C:\Brothers\Charan\Python\Youtube\ChrisThomp\SpaceInvader\pictures\SpaceInvadersLaserDepiction.gif")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(.5, .5)
bullet.hideturtle()

bulletspeedis=s

bulletstate=("ready")


Wingame=30

gameover=0

q=1


def move_left():
    x=player.xcor()
    x=x-playerspeed
    if x<-265:
        x=-265
    player.setx(x)

def move_right():
    x=player.xcor()
    x=x+playerspeed
    if x>265:
        x=265
    player.setx(x)

'''def move_up():
    y=player.ycor()
    y=y+playerspeed
    if y>280:
        y=280
    player.sety(y)

def move_down():
    y=player.ycor()
    y=y-playerspeed
    if y<-280:
        y=-280
    player.sety(y)'''


def fire_bullet():
    global bulletstate
    if bulletstate=="ready":
        play_sound("C:\Brothers\Charan\Python\Youtube\ChrisThomp\SpaceInvader\Music\laser.wav")
        bulletstate="fire"
        x=player.xcor()
        y=10+player.ycor()
        bullet.setposition(x, y)
        bullet.showturtle()

def lower_speed_of_bullet():
    global s
    s=s-.1
    s=round(s,2)
    if s<0:
        s=0
    bulletspeed.clear()
    bulletspeedstring="Bullet Speed:" + str(s)
    bulletspeed.write(bulletspeedstring, False, align="left", font=("Arial", 11, "normal"))

def raise_speed_of_bullet(r):
    global s
    s=s+r
    s=round(s,2)
    if s>2:
        s=2
    bulletspeed.clear()
    bulletspeedstring="Bullet Speed:" + str(s)
    bulletspeed.write(bulletspeedstring, False, align="left", font=("Arial", 11, "normal"))

def is_collision(t1, t2):
    distance=math.sqrt(((t1.xcor()-t2.xcor())**2)+((t1.ycor()-t2.ycor())**2))
    if distance<15:
        return True
    else:
        return False

def play_sound(sound_file, time=0):
    winsound.PlaySound(sound_file, winsound.SND_ASYNC)
    if time>0:
        turtle.ontimer(lambda: play_sound(sound_file, time), t=int(time*1000))


wn.listen()
"""wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")"""
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
"""wn.getcanvas().bind("<Left>", move_left)
wn.getcanvas().bind("<Right>", move_right)
wn.onkey(move_up, "Up")
wn.onkey(move_down, "Down")"""
wn.onkeypress(fire_bullet, "space")
wn.onkeypress(lambda: raise_speed_of_bullet(.1), "d")
wn.onkeypress(lower_speed_of_bullet, "a")
"""wn.getcanvas().bind("<space>", fire_bullet)
wn.getcanvas().bind("<a>", raise_speed_of_bullet)
wn.getcanvas().bind("<d>", lower_speed_of_bullet)"""


pygame.mixer.init()
bgm = pygame.mixer.Sound("C:\Brothers\Charan\Python\Youtube\ChrisThomp\SpaceInvader\Music\C\H.wav")
bgm.set_volume(1.0)
bgm.play(0)
"""play_sound("C:\Brothers\Charan\Python\Youtube\ChrisThomp\SpaceInvader\Music\C\H.wav", 119)"""


def point_every_sec():
    if q==1:
        global gamescore
        gamescore=gamescore+1
        scorestring="Score:" + str(gamescore)
        score.clear()
        score.write(scorestring, False, align="left", font=("Arial", 11, "normal"))
        wn.ontimer(point_every_sec, 1000)

point_every_sec()



while True:
    wn.update()
    if gameover==1:
        High_Score_In_Space_Invader = open('High_Score_In_Space_Invader', 'r')
        content = High_Score_In_Space_Invader.read()
        High_Score_In_Space_Invader.close()
        gamescore=int(gamescore)
        content=int(content)
        if gamescore>content:
            High_Score_In_Space_Invader = open('High_Score_In_Space_Invader', 'w')
            High_Score_In_Space_Invader.write(str(gamescore))
    for enemy in enemies:
        x=enemy.xcor()
        x=x+enemyspeed
        enemy.setx(x)

        if enemy.xcor()>280:
            for e in enemies:
                y=e.ycor()
                y=y-40
                e.sety(y)
            enemyspeed=-1*enemyspeed
        if enemy.xcor()<-280:
            for e in enemies:
                y=e.ycor()
                y=y-40
                e.sety(y)
            enemyspeed=-1*enemyspeed
        '''if enemy.ycor()<-250:
            player.hideturtle()
            enemy.hideturtle()
            wn.bgpic("C:\Brothers\Charan\Python\Youtube\ChrisThomp\SpaceInvader\pictures\Game_Over.gif")
            break'''


        if is_collision(bullet, enemy):
            play_sound("C:\Brothers\Charan\Python\Youtube\ChrisThomp\SpaceInvader\Music\explosion.wav")
            bullet.hideturtle()
            bullet.setposition(-500, 500)
            bulletstate="ready"
            '''x=random.randint(-200, 200)
            y=random.randint(100,250)
            enemy.setposition(x, y)'''
            enemy.hideturtle()
            enemy.setposition(0, 1000)
            Wingame=Wingame-1
            gamescore=gamescore+5
            score.clear()
            #Can do score.clear() or score.undo()
            scorestring="Score:" + str(gamescore)
            score.write(scorestring, False, align="left", font=("Arial", 11, "normal"))
        if is_collision(player, enemy):
            q=0
            play_sound("C:\Brothers\Charan\Python\Youtube\ChrisThomp\SpaceInvader\Music\explosion.wav")
            player.hideturtle()
            player.setposition(-500, 500)
            for e in enemies:
                e.hideturtle()
                e.setposition(0, 1000)
            wn.bgpic("C:\Brothers\Charan\Python\Youtube\ChrisThomp\SpaceInvader\pictures\glitch-game-background_23-2148090006.gif")
            break
        if enemy.ycor()<-300:
            q=0
            play_sound("C:\Brothers\Charan\Python\Youtube\ChrisThomp\SpaceInvader\Music\explosion.wav")
            player.hideturtle()
            player.setposition(-500, 500)
            for e in enemies:
                e.hideturtle()
                e.setposition(0, 1000)
            wn.bgpic("C:\Brothers\Charan\Python\Youtube\ChrisThomp\SpaceInvader\pictures\glitch-game-background_23-2148090006.gif")
            break
        if enemy.ycor()>300:
            enemy.setposition(0, 1000)
        if Wingame==0:
            q=0
            gameover=1
            bullet.hideturtle()
            player.hideturtle()
            bullet.setposition(-500, 500)
            player.setposition(-500, 500)
            for e in enemies:
                e.hideturtle()
                enemy.setposition(0,1000)
            wn.bgpic("C:\Brothers\Charan\Python\Youtube\ChrisThomp\SpaceInvader\pictures\images.gif")

    if bulletstate=="fire":
        bulletspeedis=s
        y=bullet.ycor()
        y=bulletspeedis+y
        bullet.sety(y)
    if bullet.ycor()>275:
        bullet.hideturtle()
        bulletstate="ready"
        bullet.setposition(-500, 500)

#I don't even need the turtle.mainloop() becasue it never gets there becasue of the forever loop ontop.
turtle.mainloop()