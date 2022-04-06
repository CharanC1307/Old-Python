from PIL import ImageGrab, ImageOps
from numpy import *
import pyautogui
import time

class Cordinates():
    replayBTN=(990, 400)
    Dinosaur=(751, 406)

def ResartGame():
    pyautogui.click(Cordinates.replayBTN)

def PressSpace():
    pyautogui.keyDown("space")
    time.sleep(.02)
    pyautogui.keyUp("space")

def GrabImage():
    box=(805, 415, 812, 435)
    image=ImageGrab.grab(box)
    GrayImage=ImageOps.grayscale(image)
    a=array(GrayImage.getcolors())
    return a.sum()

def main():
    print("play")
    ResartGame()
    while True:
        if (GrabImage()!=387):
            print("you made the jump")
            PressSpace()
            time.sleep(.1)

main()