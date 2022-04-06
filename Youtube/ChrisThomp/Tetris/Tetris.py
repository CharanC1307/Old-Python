import os
import random
import time
import turtle


wn=turtle.Screen()
wn.title("Tetris")
wn.bgcolor("#e6e1d5")
wn.setup(width=480, height=640)
wn.tracer(0, 1)

"""wn.register_shape("C:\Brothers\Charan\Python\Youtube\ChrisThomp\SpaceInvader\pictures\coooooool.gif")
wn.register_shape("C:\Brothers\Charan\Python\Youtube\ChrisThomp\Tetris\Image\cool9.gif")
wn.register_shape("C:\Brothers\Charan\Python\Youtube\ChrisThomp\Tetris\Image\green.gif")"""



delay=.25 


class Shape():
    def __init__(self):
        self.x=5
        self.y=0
        self.color=random.randint(1, 7)
        self.square=[[1, 1],
                     [1, 1]]
        self.horizontal_line=[[1, 1, 1, 1]]
        self.left_L=[[1, 0, 0, 0],
                     [1, 1, 1, 1]]
        self.right_L=[[0, 0, 0, 1],
                      [1, 1, 1, 1]]
        self.left_S=[[1, 1, 0],
                     [0, 1, 1]]
        self.right_S=[[0, 1, 1],
                      [1, 1, 0]]
        self.T=[[0,1,0],
                [1,1,1]]
        self.shapes=[self.square, self.horizontal_line, self.left_L, self.left_S, self.right_S, self.T]
        self.shape=random.choice(self.shapes)
        self.height=len(self.shape)
        self.width=len(self.shape[0])
    def move_left(self, grid):
        if self.x>0 and grid[self.y][self.x-1]==0 and grid[self.y+self.height-1][self.x-1]==0:
            self.erase_shape(grid)
            self.x=self.x-1
            self.draw_shape(grid)
    def move_right(self, grid):
        if self.x+self.width-1<11 and grid[self.y][self.x+self.width]==0 and grid[self.y+self.height-1][self.x+self.width]==0:
            self.erase_shape(grid)
            self.x=self.x+1
            self.draw_shape(grid)
    def draw_shape(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                if self.shape[y][x]==1:
                    grid[self.y+y][self.x+x]=self.color
    def erase_shape(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                grid[self.y+y][self.x+x]=0
    def can_move(self, grid):
        for x in range(self.width):
            if self.shape[self.height-1][x]==1:
                if grid[self.y+self.height][self.x+x]!=0:
                    return False
            elif self.shape[self.height-2][x]==1:
                if grid[self.y+self.height-1][self.x+x]!=0:
                    return False
            elif self.shape[self.height-3][x]==1:
                if grid[self.y+self.height-2][self.x+x]!=0:
                    return False
        return True
    def rotate(self, grid):
        self.erase_shape(grid)
        rotated_shape=[]
        for x in range(self.width):
            new_row=[]
            for y in range(self.height-1, -1, -1):
                new_row.append(self.shape[y][x])
            rotated_shape.append(new_row)
        if self.x+self.height<12 and grid[self.y+self.width+1][x]==0:
            self.shape=rotated_shape
            self.height=len(self.shape)
            self.width=len(self.shape[0])

grid=[
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]


pen=turtle.Turtle()
pen.penup()
pen.speed(0)
pen.shape("square")
pen.setundobuffer(None)

border_pen=turtle.Turtle()


'''score_pen=turtle.Turtle()
score_pen.penup()
score_pen.speed(0)
score_pen.shape("square")
score_pen.setundobuffer(None)
'''

def draw_border(pen):
    pen.pencolor("#505050")
    pen.pensize(3)
    pen.penup()
    pen.goto(-140, 260)
    pen.pendown()
    pen.goto(-140, -240)
    pen.goto(120, -240)
    pen.goto(120, 260)
    pen.goto(-140, 260)
    pen.hideturtle()
    pen.penup()

"""
def draw_border(pen):
    pen.pencolor("#454444")
    pen.penup()
    pen.goto(-140, 260)
    pen.pendown()
    pen.goto(-140, -240)
    pen.goto(120, -240)
    pen.goto(120, 260)
    pen.goto(-140, 260)
    pen.hideturtle()
    pen.penup()"""



def draw_grid(pen, grid):
    pen.clear()
    top=240
    left=-120
    shapes=["black", "#00f0f0", "blue", "orange", "yellow", "green", "purple", "#f00000"]
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            screen_x=left+(x*20)
            screen_y=top-(y*20)
            number=grid[y][x]
            shape=shapes[number]
            pen.color(shape)
            pen.goto(screen_x, screen_y)
            pen.stamp()
"""    Pen_shapes=["C:\Brothers\Charan\Python\Youtube\ChrisThomp\Tetris\Image\green.gif", "C:\Brothers\Charan\Python\Youtube\ChrisThomp\SpaceInvader\pictures\coooooool.gif", "C:\Brothers\Charan\Python\Youtube\ChrisThomp\SpaceInvader\pictures\coooooool.gif", "C:\Brothers\Charan\Python\Youtube\ChrisThomp\SpaceInvader\pictures\coooooool.gif", "C:\Brothers\Charan\Python\Youtube\ChrisThomp\SpaceInvader\pictures\coooooool.gif", "C:\Brothers\Charan\Python\Youtube\ChrisThomp\SpaceInvader\pictures\coooooool.gif", "C:\Brothers\Charan\Python\Youtube\ChrisThomp\Tetris\Image\cool9.gif", "C:\Brothers\Charan\Python\Youtube\ChrisThomp\SpaceInvader\pictures\coooooool.gif"]
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            screen_x=left+(x*20)
            screen_y=top-(y*20)
            Shape_number=grid[y][x]
            Pen_shape=Pen_shapes[Shape_number]
            pen.shape(Pen_shape)
            pen.goto(screen_x, screen_y)
            pen.stamp()"""

def check_grid(grid):
    y=23 
    while y>0:
        is_full=True
        for x in range(0, 12):
            if grid[y][x]==0:
                is_full=False
                y=y-1
                break
        if is_full:
            global score
            score=score+10
            draw_score(pen, score)
            for copy_y in range(y, 0, -1):
                for copy_x in range(0, 12):
                    grid[copy_y][copy_x]=grid[copy_y-1][copy_x]
def draw_score(pen, score):
    pen.hideturtle()
    pen.color("blue")
    pen.goto(-55, 280)
    gamescore="Score:"+str(score)
    pen.write(gamescore, font=("Times", 24, "normal"))

shape = Shape()


wn.listen()
wn.onkeypress(lambda: shape.move_left(grid), "Left")
wn.onkeypress(lambda: shape.move_right(grid), "Right")
wn.onkeypress(lambda: shape.rotate(grid), "space")


score=0

draw_border(border_pen)

while True:
    wn.update()
    if shape.y==23-shape.height+1:
        shape=Shape()
        check_grid(grid)
    if shape.can_move(grid):
        shape.erase_shape(grid)
        shape.y=shape.y+1
        shape.draw_shape(grid)
    else:
        shape=Shape()
        check_grid(grid)
    draw_grid(pen, grid)
    draw_score(pen, score)
    time.sleep(delay)