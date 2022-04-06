import turtle

wn=turtle.Screen()
wn.bgcolor("black")

pen=turtle.Turtle()
pen.hideturtle()
pen.penup()

def draw_score(pen):
    pen.color("white")
    pen.goto(0, 300)
    pen.write("Score:", font=("Arial", 24, "normal"))
    pen.goto(-50, 250)
    pen.write("Score:", font=("Comic Sans MS", 24, "normal"))
    pen.goto(-50, 200)
    pen.write("Score:", font=("Times", 24, "normal"))
    pen.goto(-50, 150)
    pen.write("Score:", font=("Helvetica", 24, "normal"))

draw_score(pen)

turtle.mainloop()