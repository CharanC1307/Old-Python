import turtle
import random
import time
import os

os.system("cls")

delay=.1

wn=turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(700, 700)
wn.tracer(0)


head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction="stop"

food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)


def go_up():
    head.direction="up"

def go_down():
    head.direction="down"

def go_left():
    head.direction="left"

def go_right():
    head.direction="right"


def move():
    if head.direction=="up":
        head.sety(head.ycor()+20)
    if head.direction=="down":
        head.sety(head.ycor()-20)
    if head.direction=="left":
        head.setx(head.xcor()-20)
    if head.direction=="right":
        head.setx(head.xcor()+20)

wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")


while True:
    wn.update()
    move()
    """if head.xcor()=food.xcor() and head.ycor()=food.ycor():"""
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x, y)
    time.sleep(delay)