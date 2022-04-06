import pyautogui
import time
import keyboard
import random

keyboard.wait("s")
print("Start")
Play=True
TimerLimit=60
pyautogui.FAILSAFE=False
while Play:
    StartTimeHunt=time.time()
    Hunted=False
    while not Hunted:
        ElapsedTimeHunt=time.time()-StartTimeHunt
        if keyboard.is_pressed("q"):
            Play=False
        elif ElapsedTimeHunt>TimerLimit:
            pyautogui.click(408, 690)
            keyboard.write("rpg hunt")
            keyboard.press("enter")
            #time.sleep(2)
            #keyboard.write("rpg heal")
            #keyboard.press("enter")
            Hunted=True
    RandomNum=random.randint(1,3)
    TimerLimit=60
    TimerLimit=TimerLimit+RandomNum
    StartTimeHunt=time.time()
    Hunted=False
    while not Hunted:
        ElapsedTimeHunt=time.time()-StartTimeHunt
        if keyboard.is_pressed("q"):
            Play=False
        elif ElapsedTimeHunt>TimerLimit:
            pyautogui.click(408, 690)
            keyboard.write("rpg hunt")
            keyboard.press("enter")
            Hunted=True
    RandomNum=random.randint(1,3)
    TimerLimit=60
    TimerLimit=TimerLimit+RandomNum
    StartTimeHunt=time.time()
    Hunted=False
    while not Hunted:
        ElapsedTimeHunt=time.time()-StartTimeHunt
        if keyboard.is_pressed("q"):
            Play=False
        elif ElapsedTimeHunt>TimerLimit:
            pyautogui.click(408, 690)
            keyboard.write("rpg hunt")
            keyboard.press("enter")
            #time.sleep(3)
            #keyboard.write("rpg heal")
            #keyboard.press("enter")
            Hunted=True
    RandomNum=random.randint(1,3)
    TimerLimit=60
    TimerLimit=TimerLimit+RandomNum
    StartTimeHunt=time.time()
    Hunted=False
    while not Hunted:
        ElapsedTimeHunt=time.time()-StartTimeHunt
        if keyboard.is_pressed("q"):
            Play=False
        elif ElapsedTimeHunt>TimerLimit:
            pyautogui.click(408, 690)
            keyboard.write("rpg hunt")
            keyboard.press("enter")
            Hunted=True
    RandomNum=random.randint(1,3)
    TimerLimit=60
    TimerLimit=TimerLimit+RandomNum
    StartTimeAxe=time.time()
    while Hunted:
        ElapsedTimeAxe=time.time()-StartTimeAxe
        if keyboard.is_pressed("q"):
            Play=False
        elif ElapsedTimeAxe>TimerLimit:
            pyautogui.click(408, 690)
            keyboard.write("rpg axe")
            keyboard.press("enter")
            time.sleep(3)
            keyboard.write("rpg hunt")
            keyboard.press("enter")
            Hunted=False
    RandomNum=random.randint(1,3)
    TimerLimit=60
    TimerLimit=TimerLimit+RandomNum
    StartTimeHunt=time.time()
    Hunted=False
print("Done")