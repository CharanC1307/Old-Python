import pyautogui
import time
import keyboard


keyboard.wait("s")
Play=True
while Play:
    if keyboard.is_pressed("q"):
        Play=False
    else:
        keyboard.press(xs)
        time.sleep(60)
print("Done")