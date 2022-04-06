import turtle
import pyautogui
import math
import time


wn=turtle.Screen()
wn.setup(600, 600)
wn.tracer(0)


def Drag(x, y):
    if math.sqrt(((x-Joystick2.xcor())**2)+(y-Joystick2.ycor())**2)>=40:
        Joystick.goto(last_x, last_y)
    else:
        Joystick.goto(x, y)
        last_x=x
        last_y=y

def Move(x, y):
    Joystick.goto(x, y)
    Joystick2.goto(x, y)
    pyautogui.click()

def Move_Away(x, y):
    Joystick.goto(1000, 1000)
    Joystick2.goto(1000, 1000)

Joystick2=turtle.Turtle()
Joystick2.penup()
Joystick2.shape("circle")
Joystick2.speed(0)
Joystick2.shapesize(6, 6)

Joystick=turtle.Turtle()
Joystick.penup()
Joystick.shape("circle")
Joystick.color("blue")
Joystick.speed(0)
Joystick.shapesize(2, 2)
Joystick.ondrag(Drag)
Joystick.onrelease(Move_Away)

wn.onclick(Move)

while True:
    wn.update()
