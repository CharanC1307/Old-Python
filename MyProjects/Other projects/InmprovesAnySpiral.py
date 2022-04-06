import turtle  #load library 
t=turtle.Turtle()  #create instance to activate the library
t.pen #activate pen

speed=int(turtle.numinput("Speed",
    "How fast do you want the drawing to move. Choose between 1-11?"))

t.speed(speed)  #speed of pen

space=int(turtle.numinput("Space Between Lines",
    "How much space do you want between lines. Choose a number. You can say decimals."))

times=int(turtle.numinput("How Many Times",
    "How many times do you want the drawing to move."))

backroundcolor=int(turtle.numinput("Backround Color",
    "What backround color do you want the drawing to have. Answere in digits. I personally like black. 1=red. 2=orange. 3=yellow. 4=green. 5=blue. 6=purple. 7=pink. 8=white. 9=black."))

rainbow=["red","orange","yellow","green","blue","purple","pink"]
bgcolor1=""
if backroundcolor==1:
    bgcolor1="red"
elif backroundcolor==2:
    bgcolor1="orange"
elif backroundcolor==3:
    bgcolor1="yellow"
elif backroundcolor==4:
    bgcolor1="green"
elif backroundcolor==5:
    bgcolor1="blue"
elif backroundcolor==6:
    bgcolor1="purple"
elif backroundcolor==7:
    bgcolor1="black"
elif backroundcolor==8:
    bgcolor1="white"
elif backroundcolor==9:
    bgcolor1="black"

color=int(turtle.numinput("Color",
    "What color do you want the drawing to be. Answere in digits. 0=rainbow. 1=red. 2=orange. 3=yellow. 4=green. 5=blue. 6=purple. 7=pink. 8=white. 9=black."))

sides=int(turtle.numinput("sides",
    "How many sides do you want in the drawing. Up to 7 sides."))

for x in range(times):
    color1=""
    if color==0:
        color1=rainbow[x%sides]
    elif color==1:
        color1="red"
    elif color==2:
        color1="orange"
    elif color==3:
        color1="yellow"
    elif color==4:
        color1="green"
    elif color==5:
        color1="blue"
    elif color==6:
        color1="purple"
    elif color==7:
        color1="pink"
    elif color==8:
        color1="white"
    elif color==9:
        color1="black"
    turtle.bgcolor(bgcolor1)
    t.pencolor(color1)
    t.forward(space*x)  #multiply (*) x by a number to make lines more apart
    t.left(360/sides+1)
turtle.done()