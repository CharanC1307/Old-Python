import pyautogui
import time
import keyboard

keyboard.wait("s")
Play=True
while Play:
    if keyboard.is_pressed("q"):
        Play=False
    else:
        pyautogui.click(408, 690)
        keyboard.press("H")
        keyboard.press("I")
        keyboard.press("Enter")
        time.sleep(1)
print("Done")