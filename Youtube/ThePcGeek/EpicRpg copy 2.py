import pyautogui
import time
import keyboard

keyboard.wait("s")
print("Start")
Play=True
TimerLimit=60
pyautogui.FAILSAFE=False
while Play:
    if keyboard.is_pressed("q"):
        Play=False
    else:
        time.sleep(300)
        pyautogui.click(408, 690)
        keyboard.write("rpg axe")
        time.sleep(3)
        keyboard.press("enter")
print("Done")