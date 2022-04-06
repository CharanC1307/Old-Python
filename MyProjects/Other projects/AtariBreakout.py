import turtle


wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.setup(width=700, height=700)


pen=turtle.Turtle()
pen.pensize(3)
pen.hideturtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.setposition(-300,-300)
pen.pendown()
for i in range(4):
    pen.forward(600)
    pen.left(90)
pen.hideturtle()


number_of_enemies=18

enemies=[]

for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

enemy_start_x=-250
enemy_start_y=265
enemy_number=0

for enemy in enemies:
    enemy.color("red")
    enemy.penup()
    enemy.shape("square")
    enemy.shapesize(1.5,4)
    enemy.speed(0)
    x=enemy_start_x+(80*enemy_number)
    y=enemy_start_y
    enemy.setposition(x, y)
    enemy_number=enemy_number+1
    if enemy_number==6:
        enemy_number=0
        enemy_start_y=enemy_start_y-40


turtle.mainloop()