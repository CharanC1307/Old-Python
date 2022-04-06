import turtle
import math
import random


Screen_Width=800
Screen_Height=600

wn=turtle.Screen()
wn.title("Space Arena")
wn.setup(Screen_Width+220, Screen_Height+20)
wn.bgcolor("black")
wn.tracer(0)


pen=turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()


class Game():
    def __init__(self, width, height):
        self.width=width
        self.height=height
        self.level=1
    def start_level(self, sprite_list):
        sprite_list.clear()
        sprite_list.append(player)
        for bullet in bullets:
            sprite_list.append(bullet)
        for _ in range(self.level):
            x=random.randint(-self.width/2, self.width/2)
            y=random.randint(-self.height/2, self.height/2)
            dx=random.uniform(-.5, .5)
            dy=random.uniform(-.5, .5)
            dx=0
            dy=0
            sprite_list.append(Enemy(x, y, "square", "red"))
            sprite_list[-1].dx=dx
            sprite_list[-1].dy=dy
        for _ in range(self.level):
            x=random.randint(-self.width/2, self.width/2)
            y=random.randint(-self.height/2, self.height/2)
            dx=random.uniform(-.5, .5)
            dy=random.uniform(-.5, .5)
            sprite_list.append(Powerup(x, y, "circle", "blue"))
            sprite_list[-1].dx=dx
            sprite_list[-1].dy=dy
    def render_border(self, pen, x_offset, y_offset):
        pen.color("white")
        pen.width(3)
        """pen.goto(-self.width/2, -self.height/2)
        pen.pendown()
        pen.goto(self.width/2, -self.height/2)
        pen.goto(self.width/2, self.height/2)
        pen.goto(-self.width/2, self.height/2)
        pen.goto(-self.width/2, -self.height/2)"""
        left = -self.width/2.0-x_offset
        right = self.width/2.0-x_offset
        top = self.height/2.0-y_offset
        bottom = -self.height/2.0-y_offset
        pen.goto(left, top)
        pen.pendown()
        pen.goto(right, top)
        pen.goto(right, bottom)
        pen.goto(left, bottom)
        pen.goto(left, top)
        pen.penup()
    def render_info(self, pen, score, writing_method, lives, level, active_enemies=0):
        pen.color("#222255")
        pen.penup()
        pen.goto(400, 0)
        pen.shape("square")
        pen.setheading(90)
        pen.shapesize(10, 32, None)
        pen.stamp()
        pen.color("white")
        pen.width(3)
        pen.goto(300, 400)
        pen.pendown()
        pen.goto(300, -400)
        pen.penup()
        writing_method.scale=1
        writing_method.draw_string(pen, "SPACE ARENA", 400, 270)
        writing_method.draw_string(pen, "SCORE "+str(score), 400, 240)
        writing_method.draw_string(pen, "ENEMIES "+str(active_enemies), 400, 210)
        writing_method.draw_string(pen, "LIVES "+str(lives), 400, 180)
        writing_method.draw_string(pen, "LEVEL "+str(level), 400, 150)

class CharacterPen():
    def __init__(self, color="white", scale=1.0):
        self.color=color
        self.scale=scale
        self.characters = {}
        self.characters["1"] = ((-5, 10), (0, 10), (0, -10), (-5, -10), (5, -10))
        self.characters["2"] = ((-5, 10),(5, 10),(5, 0), (-5, 0), (-5, -10), (5, -10))
        self.characters["3"] = ((-5, 10),(5, 10),(5, 0), (0, 0), (5, 0), (5,-10), (-5, -10))
        self.characters["4"] = ((-5, 10), (-5, 0), (5, 0), (2,0), (2, 5), (2, -10))
        self.characters["5"] = ((5, 10), (-5, 10), (-5, 0), (5,0), (5,-10), (-5, -10))
        self.characters["6"] = ((5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0), (-5, 0))
        self.characters["7"] = ((-5, 10), (5, 10), (0, -10))
        self.characters["8"] = ((-5, 0), (5, 0), (5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0))
        self.characters["9"] = ((5, -10), (5, 10), (-5, 10), (-5, 0), (5, 0))
        self.characters["0"] = ((-5, 10), (5, 10), (5, -10), (-5, -10), (-5, 10))
        self.characters["A"] = ((-5, -10), (-5, 10), (5, 10), (5, -10), (5, 0), (-5, 0))
        self.characters["B"] = ((-5, -10), (-5, 10), (3, 10), (3, 0), (-5, 0), (5,0), (5, -10), (-5, -10))
        self.characters["C"] = ((5, 10), (-5, 10), (-5, -10), (5, -10))
        self.characters["D"] = ((-5, 10), (-5, -10), (5, -8), (5, 8), (-5, 10))
        self.characters["E"] = ((5, 10), (-5, 10), (-5, 0), (0, 0), (-5, 0), (-5, -10), (5, -10))
        self.characters["F"] = ((5, 10), (-5, 10), (-5, 0), (5, 0), (-5, 0), (-5, -10))
        self.characters["G"] = ((5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0), (0, 0))
        self.characters["H"] = ((-5, 10), (-5, -10), (-5, 0), (5, 0), (5, 10), (5, -10))
        self.characters["I"] = ((-5, 10), (5, 10), (0, 10), (0, -10), (-5, -10), (5, -10))
        self.characters["J"] = ((5, 10), (5, -10), (-5, -10), (-5, 0))
        self.characters["K"] = ((-5, 10), (-5, -10), (-5, 0), (5, 10), (-5, 0), (5, -10))
        self.characters["L"] = ((-5, 10), (-5, -10), (5, -10))
        self.characters["M"] = ((-5, -10), (-3, 10), (0, 0), (3, 10), (5, -10))
        self.characters["N"] = ((-5, -10), (-5, 10), (5, -10), (5, 10))
        self.characters["O"] = ((-5, 10), (5, 10), (5, -10), (-5, -10), (-5, 10))
        self.characters["P"] = ((-5, -10), (-5, 10), (5, 10), (5, 0), (-5, 0))
        self.characters["Q"] = ((5, -10), (-5, -10), (-5, 10), (5, 10), (5, -10), (2, -7), (6, -11))
        self.characters["R"] = ((-5, -10), (-5, 10), (5, 10), (5, 0), (-5, 0), (5, -10))
        self.characters["S"] = ((5, 8), (5, 10), (-5, 10), (-5, 0), (5, 0), (5, -10), (-5, -10), (-5, -8))
        self.characters["T"] = ((-5, 10), (5, 10), (0, 10), (0, -10))
        self.characters["V"] = ((-5, 10), (0, -10), (5, 10))
        self.characters["U"] = ((-5, 10), (-5, -10), (5, -10), (5, 10))
        self.characters["W"] = ((-5, 10), (-3, -10), (0, 0), (3, -10), (5, 10))
        self.characters["X"] = ((-5, 10), (5, -10), (0, 0), (-5, -10), (5, 10))
        self.characters["Y"] = ((-5, 10), (0, 0), (5, 10), (0,0), (0, -10))
        self.characters["Z"] = ((-5, 10), (5, 10), (-5, -10), (5, -10))
        self.characters["-"] = ((-3, 0), (3, 0))
    def draw_string(self, pen, string, x, y):
        pen.width(2)
        pen.color(self.color)
        x = x-(15*self.scale*((len(string)-1)/2))
        for character in string:
            self.draw_character(pen, character, x, y)
            x=15*self.scale+x
    def draw_character(self, pen, character, x, y):
        scale=self.scale
        pen.width(2)
        if character in "abcdefghijklmnopqrstuvwxyz":
            scale *= 0.8
        character=character.upper()
        if character in self.characters:
            pen.penup()
            xy=self.characters[character][0]
            pen.goto(x+xy[0]*scale, y+xy[1]*scale)
            pen.pendown()
            for i in range(1, len(self.characters[character])):
                xy=self.characters[character][i]
                pen.goto(x+xy[0]*scale, y+xy[1]*scale)
            pen.penup()

class Sprite():
    def __init__(self, x, y, shape, color):
        self.acceleration=.075
        self.max_health=100
        self.state="active"
        self.shapeheight=1
        self.shapewidth=1
        self.shape=shape
        self.color=color
        self.health=100
        self.radar=500
        self.heading=0
        self.height=20
        self.max_dx=2.5
        self.max_dy=2.5
        self.thrust=0
        self.width=20
        self.dx=0
        self.dy=0
        self.da=0
        self.x=x
        self.y=y
    def is_collision(self, other):
        if self.x < other.x + other.width and\
            self.x + self.width > other.x and\
            self.y < other.y + other.height and\
            self.y + self.height > other.y:
            return True
        else:
            return False
    def bounce(self, other):
        temp_dx=self.dx
        temp_dy=self.dy
        self.dx=other.dx
        self.dy=other.dy
        other.dx=temp_dx
        other.dy=temp_dy
    def update(self, width, height):
        if self.state=="active":
            self.heading=self.heading+self.da
            self.heading=self.heading%360
            self.dx=self.dx+(math.cos(math.radians(self.heading))*self.thrust)
            self.dy=self.dy+(math.sin(math.radians(self.heading))*self.thrust)
            self.x=self.x+self.dx
            self.y=self.y+self.dy
            self.border_check(width, height)
            if self.health<=0:
                self.reset()
        #self.da=0
    def border_check(self, width, height):
        if self.x>width/2-10:
            self.x=width/2-10
            self.dx=self.dx*-1
        elif self.x<-width/2+10:
            self.x=-width/2+10
            self.dx=self.dx*-1
        if self.y>height/2-10:
            self.y=height/2-10
            self.dy=self.dy*-1
        elif self.y<-height/2+10:
            self.y=-height/2+10
            self.dy=self.dy*-1
    def render(self, pen, x_offset, y_offset):
        if self.state=="active":
            pen.shapesize(self.shapewidth, self.shapeheight, None)
            pen.goto(self.x-x_offset, self.y-y_offset)
            pen.setheading(self.heading)
            pen.shape(self.shape)
            pen.color(self.color)
            pen.stamp()
            self.render_health_meter(pen, x_offset, y_offset)
    def render_health_meter(self, pen, x_offset, y_offset):
        pen.width(3)
        """health_heading=self.heading-90
        pen.setheading(health_heading)"""
        pen.setheading(0)
        pen.goto(self.x-x_offset-10, self.y-y_offset-20)
        pen.pendown()
        if self.health/self.max_health<0.33:
            pen.color("red")
        elif self.health/self.max_health<0.66:
            pen.color("yellow")
        else:
            pen.color("#27d600")
        cool=20*(self.health/self.max_health)
        pen.fd(cool)
        """pen.color("grey")
        pen.fd(20-cool)"""
        if self.health != self.max_health:
            pen.color("grey")
            pen.fd(20.0 * ((self.max_health-self.health)/self.max_health))
        pen.penup()
    def reset(self):
        self.state="inactive"

class Player(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)
        self.shapeheight=1
        self.shapewidth=.5
        self.heading=90
        self.height=20
        self.width=10
        self.lives=3
        self.score=0
        self.da=0
    def rotate_left(self):
        self.da=6
    def rotate_right(self):
        self.da=-6
    def stop_rotation(self):
        self.da=0
    def accelerate(self):
        self.thrust=self.thrust+self.acceleration
    def decelerate(self):
        self.thrust=0
    def stop(self):
        self.dx=0
        self.dy=0
    def fire(self, bullet):
        was_heading=self.heading
        self.heading=self.heading-10
        for bullet in bullets:
            bullet.fire(self.x, self.y, self.heading, self.dx, self.dy)
            self.heading=self.heading+10
        self.heading=was_heading
    def reset(self):
        self.health=self.max_health
        self.lives=self.lives-1
        self.heading=90
        self.dx=0
        self.dy=0
        self.x=0
        self.y=0

class Bullet(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)
        self.shapeheight=.2
        self.shapewidth=.2
        self.state="ready"
        self.max_fuel=200
        self.height=4
        self.thrust=6
        self.fuel=200
        self.width=4
    def fire(self, x, y, heading, dx, dy):
        if self.state=="ready":
            self.state="active"
            self.heading=heading
            self.dx=dx
            self.dy=dy
            self.x=x
            self.y=y
            self.dx=self.dx+(math.cos(math.radians(self.heading))*self.thrust)
            self.dy=self.dy+(math.sin(math.radians(self.heading))*self.thrust)
    def update(self, width, height):
        if self.state=="active":
            self.fuel=self.fuel-self.thrust
            if self.fuel<=0:
                self.reset()
            self.heading=self.heading+self.da
            self.heading=self.heading%360
            self.x=self.x+self.dx
            self.y=self.y+self.dy
            self.border_check(width, height)
    def render(self, pen, x_offset, y_offset):
        if self.state=="active":
            pen.shapesize(self.shapewidth, self.shapeheight, None)
            pen.goto(self.x-x_offset, self.y-y_offset)
            pen.setheading(self.heading)
            pen.shape(self.shape)
            pen.color(self.color)
            pen.stamp()
    def reset(self):
        self.fuel=self.max_fuel
        self.dx=0
        self.dy=0
        self.state="ready"

class Enemy(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)
        self.max_health=20
        self.health=self.max_health
        self.type=random.choice(["hunter", "mine", "surveillance"])
        if self.type=="hunter":
            self.color="red"
            self.shape="square"
        elif self.type=="mine":
            self.color="orange"
            self.shape="square"
        elif self.type=="surveillance":
            self.color="pink"
            self.shape="square"
    def update(self, width, height):
        if self.state=="active":
            self.heading=self.heading+self.da
            self.heading=self.heading%360
            self.dx=self.dx+(math.cos(math.radians(self.heading))*self.thrust)
            self.dy=self.dy+(math.sin(math.radians(self.heading))*self.thrust)
            self.x=self.x+self.dx
            self.y=self.y+self.dy
            self.border_check(width, height)
            if self.health<=0:
                self.reset()
            if self.type=="hunter":
                if self.x<player.x:
                    self.dx=self.dx+.025
                else:
                    self.dx=self.dx-.025
                if self.x<player.y:
                    self.dy=self.dy+.025
                else:
                    self.dy=self.dy-.025
            elif self.type=="mine":
                self.dx=0
                self.dy=0
            elif self.type=="surveillance":
                if self.x<player.x:
                    self.dx=self.dx-.025
                else:
                    self.dx=self.dx+.025
                if self.x<player.y:
                    self.dy=self.dy-.025
                else:
                    self.dy=self.dy+.025
            if self.dx>self.max_dx:
                self.dx=self.max_dx
            elif self.dx<-self.max_dx:
                self.dx=-self.max_dx
            if self.dy>self.max_dy:
                self.dy=self.max_dy
            if self.dy<-self.max_dy:
                self.dy=-self.max_dy

class Powerup(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)

class Camera():
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def update(self, x, y):
        self.x=x
        self.y=y

class Radar():
    def __init__(self, x, y, width, height):
        self.height=height
        self.width=width
        self.x=x
        self.y=y
    def render(self, pen, sprite_list, width, height):
        pen.color("white")
        pen.width(2)
        pen.setheading(90)
        pen.goto(self.x+self.width/2, self.y)
        pen.pendown()
        pen.circle(self.width/2)
        pen.penup()
        for sprite in sprite_list:
            if sprite.state=="active":
                radar_x=self.x+(sprite.x-player.x)*(self.width/game.width)
                radar_y=self.y+(sprite.y-player.y)*(self.height/game.height)
                pen.goto(radar_x, radar_y)
                pen.color(sprite.color)
                pen.shape(sprite.shape)
                pen.setheading(sprite.heading)
                pen.shapesize(sprite.shapewidth/5, sprite.shapeheight/5, None)
                distance=((player.x-sprite.x)**2+(player.y-sprite.y)**2)**.5
                if distance<player.radar:
                    pen.stamp()


game=Game(750, 500)

character_pen=CharacterPen("red", 3)

player=Player(0, 0, "triangle", "white")

bullets=[]
for _ in range(1):
    bullets.append(Bullet(0, 100, "circle", "yellow"))

camera=Camera(player.x, player.y)

radar=Radar(400, -200, 200, 200)

sprites=[]

game.start_level(sprites)

def quit():
    global running
    running=False


wn.listen()
wn.onkeypress(player.rotate_left, "Left")
wn.onkeypress(player.rotate_right, "Right")
wn.onkeyrelease(player.stop_rotation, "Left")
wn.onkeyrelease(player.stop_rotation, "Right")
wn.onkeypress(player.accelerate, "Up")
wn.onkeyrelease(player.decelerate, "Up")
wn.onkeypress(player.stop, "Down")
wn.onkeypress(lambda: player.fire(bullet), "space")
wn.onkey(quit, "q")
wn.onkey(quit, "Q")


running=True

while running:
    pen.clear()
    for sprite in sprites:
        sprite.update(game.width, game.height)
    for sprite in sprites:
        if isinstance(sprite, Enemy) and sprite.state=="active":
            if player.is_collision(sprite):
                sprite.health=sprite.health-10
                player.health=player.health-10
                player.bounce(sprite)
            for bullet in bullets:
                if bullet.state=="active" and bullet.is_collision(sprite):
                    sprite.health=sprite.health-10
                    bullet.reset()
        if isinstance(sprite, Powerup):
            if player.is_collision(sprite):
                player.bounce(sprite)
            for bullet in bullets:
                if bullet.state=="active" and bullet.is_collision(sprite):
                    sprite.x=100
                    sprite.y=-100
                    bullet.reset()
    for sprite in sprites:
        sprite.render(pen, camera.x+100, camera.y)
    game.render_border(pen, camera.x+100, camera.y)
    active_enemies=game.level
    end_of_level=True
    for sprite in sprites:
        if isinstance(sprite, Enemy) and sprite.state=="active":
            end_of_level=False
        elif isinstance(sprite, Enemy) and sprite.state=="inactive":
            active_enemies=active_enemies-1
    if end_of_level:
        game.level=game.level+1
        game.start_level(sprites)
    camera.update(player.x, player.y)
    game.render_info(pen, 0, character_pen, player.lives, game.level, active_enemies)
    radar.render(pen, sprites, game.width, game.height)
    pen.goto(0, 0)
    wn.update()