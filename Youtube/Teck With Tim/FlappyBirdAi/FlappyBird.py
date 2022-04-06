from hashlib import new
from cv2 import rotate
from more_itertools import consecutive_groups
import pygame
import neat
import time
import os
import random
from PIL import Image

#A convention to make constants and such fully captalized.

os.chdir("C:\Brothers\Charan\Code\Python\Youtube\Teck With Tim\FlappyBirdAi")

WIN_WIDTH=600
Win_HEIGHT=800

#Could use a for loop for the BIRD_IMGS to improve readability.
BIRD_IMGS=[pygame.transform.scale2x(pygame.image.load("img/bird1.png")), pygame.transform.scale2x(pygame.image.load("img/bird2.png")),pygame.transform.scale2x(pygame.image.load("img/bird3.png"))]
PIPE_IMG=pygame.transform.scale2x(pygame.image.load("img/pipe.png"))
BASE_IMG=pygame.transform.scale2x(pygame.image.load("img/base.png"))
BG_IMG=pygame.transform.scale2x(pygame.image.load("img/bg.png"))

class Bird():
    def __init__(self, x, y):
        self.IMGS=BIRD_IMGS
        self.MAX_ROTATION=25
        self.ROT_VEL=20
        self.ANIMATION_TIME=5
        self.x=x
        self.y=y
        self.tilt=0
        self.tick_count=0
        self.vel=0
        self.height=self.y
        self.img_count=0
        self.img=self.IMGS[0]
    
    #Since 0,0 is at the top left of the screen. a negative velocity makes it go upwards and a postitiv velocity makes it go downward.
    #Plus equal self.vel so every time I press it goes down and isn't static. THIS IS WRONG. Don't read this to myself lol.
    def jump(self):
        self.vel=-10.5
        self.tick_count=0
        self.height=self.y

    def move(self):
        self.tick_count+=1

        d=self.vel*self.tick_count+1.5*self.tick_count**2
        if d>=16:
            d=16
        if d<0:
            d-=2

        self.y=self.y+d
        if d<0 or self.y<self.height+50:
            if self.tilt<self.MAX_ROTATION:
                self.tilt=self.MAX_ROTATION
        else:
            if self.tilt>-90:
                self.tilt=+self.ROT_VEL
    
    #clean this function up
    def draw(self,win):
        self.img_count+=1

        if self.img_count<self.ANIMATION_TIME:
            self.img=self.IMGS[0]
        elif self.img_count<self.ANIMATION_TIME*2:
            self.img=self.IMGS[1]
        elif self.img_count<self.ANIMATION_TIME*3:
            self.img=self.IMGS[2]
        elif self.img_count<self.ANIMATION_TIME*4:
            self.img=self.IMGS[3]
        elif self.img_count==self.ANIMATION_TIME*4+1:
            self.img=self.IMGS[0]

        if self.tilt<=-80:
            self.img=self.img[1]
            self.img_count=self.ANIMATION_TIME*2

        #understand this
        rotated_image=pygame.transform.rotate(self.img, self.tilt)
        new_rect=rotated_image.get_rect(center=self.img.get_rect(topLeft=(self.x,self.y)).center)
        win.blit(rotated_image, new_rect.topLeft)

    def get_hit(self):
        return pygame.Mask.from_surface(self.img)

def draw_window(win, bird):
    win.blit(BG_IMG, ())

    pygame.display.update()


def main():
    pygame.display.update()


