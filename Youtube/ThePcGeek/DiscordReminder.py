import pyautogui
import time
import keyboard
import winsound
from win10toast import ToastNotifier

keyboard.wait("s")
toaster = ToastNotifier()
print("Start")
Play=True
while Play:
    if keyboard.is_pressed("+"):
        Play=False
    else:
        winsound.Beep(3000, 2000)
        toaster.show_toast("Do IT")
        keyboard.wait("/")
        print("cool")
        time.sleep(45)
print("Done")