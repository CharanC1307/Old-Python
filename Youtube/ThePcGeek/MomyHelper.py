import pyautogui
import random
import time
import keyboard

keyboard.wait("s")
Play=True
Moves=["click","a","b","c","d","e","f","g","h","i","j","k","l","m","click","n","o","p","q","r","s","t","u","v","w","x","y","z","click","0","1","2","3","4","5","click","6","7","8","9","space","click"]
while Play:
    if keyboard.is_pressed("q"):
        Play=False
    else:
        Move=random.choice(Moves)
        if Move=="click":
            x=random.randint(35, 65)
            y=random.randint(0, 735)
            pyautogui.click(x, y)
        else:
            pyautogui.keyDown(Move)
            time.sleep(.1)
            pyautogui.keyUp(Move)
        time.sleep(1)
print("Done")