import turtle
import os


os.system("cls")


wn=turtle.Screen()
wn.title("Flappy Bird")
wn.bgcolor("blue")
wn.setup(width=450, height=700)


player=turtle.Turtle()
player.speed()
player.color("yellow")
player.shape("turtle")
player.shapesize(3, 3)
player.penup()
player.goto(-175, 0)
player.dx=0
player.dy=0


def quit():
    global running
    running=False


wn.listen()
wn.onkeypress(quit, "q")


running=True
while running:
    wn.update()