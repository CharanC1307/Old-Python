import turtle


wn = turtle.Screen()
wn.title("How to Make a Scrolling Background")
wn.setup(height=320, width=800)
wn.tracer(0)

wn.register_shape("C:\Brothers\Charan\Python\Youtube\ChrisThomp\ScrollingBackround\Images\qackground.gif")


# Draw ground
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(3)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.shape("C:\Brothers\Charan\Python\Youtube\ChrisThomp\ScrollingBackround\Images\qackground.gif")
pen.stamp()
pen.goto(0,0)

player = turtle.Turtle()
player.speed(0)
player.shape("turtle")
player.color("yellow")
player.shapesize(2, 2)
player.setheading(0)
player.penup()
player.goto(0,-120)


camera_x=0


def left():
    global camera_x
    player.setheading(180)
    camera_x=camera_x+5

def right():
    global camera_x
    player.setheading(0)
    camera_x=camera_x-5


wn.listen()
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")


while True:
    wn.update()
    """if camera_x==800:
        camera_x=0"""
    camera_x=camera_x%800
    pen.clear()
    pen.setx(camera_x-800)
    pen.stamp()
    pen.setx(camera_x)
    pen.stamp()