import turtle

wn=turtle.Screen()
wn.setup(width=700, height=700)

player=turtle.Turtle()
player.shape("triangle")
player.speed(0)
player.setheading(90)

playerspeed=15

z=1
def press_space():
    global z
    z=z*-1
    if z==1:
        player.color("black")
    if z==-1:
        player.color("white")


def move_left():
    x=player.xcor()
    x=x-playerspeed
    if x<-280:
        x=-280
    player.setx(x)

def move_right():
    x=player.xcor()
    x=x+playerspeed
    if x>280:
        x=280
    player.setx(x)

def move_up():
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
    player.sety(y)

turtle.listen()
turtle.onkey(press_space, "space")
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(move_up, "Up")
turtle.onkey(move_down, "Down")

cool=turtle.Turtle()
while True:
    x=turtle.xcor()
    y=turtle.ycor()
    print(str(x)+","+str(y))