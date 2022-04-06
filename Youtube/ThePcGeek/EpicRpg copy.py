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
        time.sleep(3620)
        pyautogui.click(408, 690)
        keyboard.write("rpg heal")
        keyboard.press("enter")
        time.sleep(4)
        keyboard.write("rpg adventure")
        keyboard.press("enter")
        time.sleep(3620)
        pyautogui.click(408, 690)
        keyboard.write("rpg adventure")
        keyboard.press("enter")
        time.sleep(3630)
        pyautogui.click(408, 690)
        keyboard.write("rpg heal")
        keyboard.press("enter")
        time.sleep(4)
        keyboard.write("rpg adventure")
        keyboard.press("enter")
        time.sleep(5)
        keyboard.write("rpg buy epic lootbox")
        keyboard.press("enter")
print("Done")