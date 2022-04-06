import turtle

pen=turtle.Turtle()
pen.forward(100)

wn=turtle.Screen()
def exit():
    pen.reset()

wn.listen()
wn.onkeypress(exit, "q")



wn.mainloop()
"""
import turtle
turtle.fd(0)

#Create empty list
turtles =[]

#Append turtles
turtles.append(turtle.Turtle())
turtles.append(turtle.Turtle())
turtles.append(turtle.Turtle())

#Move the turtles
turtles[0].lt(90)
turtles[1].rt(90)

turtles[0].fd(100)
turtles[1].fd(100)
turtles[2].fd(100)

#Delete a turtle
#Delete the turtle trail (if any)
turtles[2].
#Hide the turtle

#Delete the turtle object
del turtles[2]

#Keep the window open
delay = input("Press enter to continue.")"""