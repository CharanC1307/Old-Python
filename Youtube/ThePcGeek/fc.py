import pyautogui
import winsound
from win10toast import ToastNotifier
toaster = ToastNotifier()
toaster.show_toast("Sample Notification","Python is awesome!!!")
winsound.Beep(5000, 1000)