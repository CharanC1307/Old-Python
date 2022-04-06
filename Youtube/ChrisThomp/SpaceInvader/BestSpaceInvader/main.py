from Stuff.Classes import Game, Player, Bullet, Enemies, turtle, winsound, time, os
import pygame


dirpath=(os.path.dirname(os.path.abspath(__file__)))
picpath=dirpath+"/Stuff/Pictures/"
musicpath=dirpath+"/Stuff/Music/"


wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.setup(width=700, height=700)
wn.bgpic(picpath+"space_invaders_background.gif")
wn.tracer(0)

wn.register_shape(picpath+"spaceship.gif")
wn.register_shape(picpath+"SpaceInvadersLaserDepiction.gif")
wn.register_shape(picpath+"invader1.gif")
wn.register_shape(picpath+"invader2.gif")


pen=turtle.Turtle()
pen.penup()
pen.setposition(-300, -300)
pen.pensize(3)
pen.hideturtle()
pen.speed(0)
pen.color("white")
pen.pendown()
for i in range(4):
    pen.forward(600)
    pen.left(90)


game=Game("blue", -300, -300)

Score=Game("white", -300, 330)
score=0
Score.write_word("left", "Score", score)

highscore=open(dirpath+"/Stuff/High_Score_In_Space_Invader_CC", "r")
highscore=highscore.read()
high_score=Game("white", -300, 315)
high_score.write_word("left", "High Score", highscore)


player=Player(picpath+"spaceship.gif", 0, -260)

bullet=Bullet(picpath+"SpaceInvadersLaserDepiction.gif", -1000, 1000)
bullet_speed=Game("white", -300, 300)
bullet_speed.write_word("left", "Bullet Speed", bullet.speed)

enemies=[]
wingame=30
enemy_start_x=-210
enemy_start_y=265
enemy_number=0
enemyspeed=.125
for i in range (wingame):
    e=Enemies(picpath+"invader1.gif", picpath+"invader2.gif", -210, 260)
    enemies.append(e)
for enemy in enemies:
    enemy.animate()
    x=enemy_start_x+(50*enemy_number)
    y=enemy_start_y
    enemy.setposition(x, y)
    enemy_number=enemy_number+1
    if enemy_number==10:
        enemy_number=0
        enemy_start_y=enemy_start_y-40


#winsound.PlaySound("C:\Brothers\Charan\Python\Youtube\ChrisThomp\SpaceInvader\Music\C\H.wav", winsound.SND_LOOP+winsound.SND_ASYNC)
pygame.mixer.init()
bgm = pygame.mixer.Sound(musicpath+"H.wav")
bgm.set_volume(1.0)
bgm.play(0)


def point_every_sec():
    global score
    if games=="play":
        score=score+1
        Score.rewrite(score)
        wn.ontimer(point_every_sec, 1000)

def quit():
    global running
    running=False


wn.listen()
wn.onkeypress(lambda: player.move("left"), "Left")
wn.onkeypress(lambda: player.move("right"), "Right")
wn.onkeypress(lambda: bullet.fire_bullet(player, musicpath+"laser.wav"), "space")
wn.onkeypress(lambda: bullet.lower_speed_of_bullet(bullet_speed.rewrite), "a")
wn.onkeypress(lambda: bullet.raise_speed_of_bullet(bullet_speed.rewrite), "d")
wn.onkeypress(quit, "q")


running=True
games="play"
point_every_sec()


while running:
    wn.update()
    if games=="play":
        for enemy in enemies:
            enemy.setx((enemy.xcor())+(enemyspeed))
            if enemy.xcor()>280:
                for e in enemies:
                    e.sety(e.ycor()-40)
                enemyspeed=enemyspeed*-1
            if enemy.xcor()<-280:
                for e in enemies:
                    e.sety(e.ycor()-40)
                enemyspeed=enemyspeed*-1
            if bullet.distance(enemy)<15:
                winsound.PlaySound(musicpath+"explosion.wav", winsound.SND_ASYNC)
                bullet.setposition(-1000, 1000)
                enemy.setposition(0, 1000)
                wingame=wingame-1
                score=score+5
                Score.rewrite(score)
            if player.distance(enemy)<15:
                games="lose"
                winsound.PlaySound(musicpath+"explosion.wav", winsound.SND_ASYNC)
            if enemy.ycor()<-300:
                games="lose"
                winsound.PlaySound(musicpath+"explosion.wav", winsound.SND_ASYNC)
            if wingame==0:
                games="win"
            if enemy.ycor()>300:
                enemy.setposition(0, 1000)
        bullet.move(bullet.speed)
    elif games=="win":
        bullet.setposition(-1000, 1000)
        player.setposition(-1000, 1000)
        for e in enemies:
            e.setposition(0, 1000)
        wn.bgpic(picpath+"images.gif")
        if int(score)>int(highscore):
            write_highscore=open(dirpath+"/Stuff/High_Score_In_Space_Invader_CC", "w")
            write_highscore.write(str(score))
    elif games=="lose":
        player.setposition(-1000, 1000)
        for e in enemies:
            e.setposition(0, 1000)
        wn.bgpic(picpath+"glitch-game-background_23-2148090006.gif")