import turtle
import random
import math


wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Chase Game")
wn.setup(width=700, height=700)
wn.tracer(0)


pen=turtle.Turtle()
pen.pen
pen.hideturtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.setposition(-300,-300)
pen.pendown()
for i in range(4):
    pen.forward(600)
    pen.left(90)


player=turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(-50, -250)
player.setheading(90)

playerspeed=15


enemies=[]

def point_every_sec():
    global enemyspeed
    enemy=turtle.Turtle()
    enemies.append(enemy)
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x=random.randint(-270, 270)
    y=random.randint(-270, 270)
    enemy.setposition(x, y)
    distance1=math.sqrt(((player.xcor()-enemy.xcor())**2)+((player.ycor()-enemy.ycor())**2))
    if distance1<200:
        distance1=math.sqrt(((player.xcor()-enemy.xcor())**2)+((player.ycor()-enemy.ycor())**2))
        enemy.setposition(x, y)
    enemyspeed=enemyspeed+.01
    wn.ontimer(point_every_sec, 3000)

enemyspeed=.1

point_every_sec()

game="play"

def move_left():
    x=player.xcor()
    x=x-playerspeed
    if x<-280:
        x=-280
    player.setx(x)
    player.setheading(180)

def move_right():
    x=player.xcor()
    x=x+playerspeed
    if x>280:
        x=280
    player.setx(x)
    player.setheading(0)

def move_up():
    y=player.ycor()
    y=y+playerspeed
    if y>280:
        y=280
    player.sety(y)
    player.setheading(90)

def move_down():
    y=player.ycor()
    y=y-playerspeed
    if y<-280:
        y=-280
    player.sety(y)
    player.setheading(270)

def is_collision(t1, t2):
    distance2=math.sqrt(((t1.xcor()-t2.xcor())**2)+((t1.ycor()-t2.ycor())**2))
    if distance2<15:
        return True
    else:
        return False


wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")

while True:
    wn.update()
    for enemy in enemies:
        if player.xcor()>enemy.xcor():
            x=enemy.xcor()
            x=x+enemyspeed
            enemy.setx(x)
        if player.xcor()<enemy.xcor():
            x=enemy.xcor()
            x=x-enemyspeed
            enemy.setx(x)
        if player.ycor()>enemy.ycor():
            y=enemy.ycor()
            y=y+enemyspeed
            enemy.sety(y)
        if player.ycor()<enemy.ycor():
            y=enemy.ycor()
            y=y-enemyspeed
            enemy.sety(y)
        if is_collision(player, enemy):
            game="gameover"
            player.hideturtle()
            for enemy in enemies:
                enemy.hideturtle()

wn.mainloop()