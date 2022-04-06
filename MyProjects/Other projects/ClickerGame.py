import turtle
import math


turtle.delay(0)


wn=turtle.Screen()
wn.bgcolor("white")
wn.title("Space Invaders")
wn.setup(width=700, height=700)


circle=turtle.Turtle()
circle.hideturtle()
circle.penup()
circle.sety(-30)
circle.speed(0)
circle.fillcolor("yellow")
circle.begin_fill()
circle.pendown()
circle.circle(30)
circle.end_fill()


rectangle=turtle.Turtle()
rectangle.hideturtle()
rectangle.penup()
rectangle.setpos(220, 330)
rectangle.speed(0)
rectangle.pendown()
for i in range(2):
    rectangle.forward(120)
    rectangle.right(90)
    rectangle.forward(60)
    rectangle.right(90)


gamescore=0

score=turtle.Turtle()
score.speed(0)
score.color("black")
score.penup()
score.setposition(-345, 330)
score.hideturtle()

scorestring="Score:" + str(gamescore)
score.write(scorestring, False, align="left", font=("Arial", 11, "normal"))


clickme=turtle.Turtle()
clickme.speed(0)
clickme.color("black")
clickme.penup()
clickme.setposition(-27, -4.5)
clickme.hideturtle()

clickmestring="Click Here"
clickme.write(clickmestring, False, align="left", font=("Arial", 9, "normal"))


clicker=turtle.Turtle()
clicker.speed(0)
clicker.color("black")
clicker.penup()
clicker.setposition(-345, 330)
clicker.hideturtle()

clickerstring="Score:" + str(gamescore)
clicker.write(clickerstring, False, align="left", font=("Arial", 11, "normal"))


def Click(x, y):
    global gamescore
    distance=math.sqrt(((0-x)**2)+((0-y)**2))
    if distance<=30:
        gamescore=gamescore+1
        scorestring="Score:" + str(gamescore)
        score.clear()
        score.write(scorestring, False, align="left", font=("Arial", 11, "normal"))


def Click_Clicker(x, y):
    global gamescore
    distance=math.sqrt(((0-x)**2)+((0-y)**2))
    if distance<=30:
        gamescore=gamescore+1
        scorestring="Score:" + str(gamescore)
        score.clear()
        score.write(scorestring, False, align="left", font=("Arial", 11, "normal"))


turtle.onscreenclick(Click)


turtle.mainloop()