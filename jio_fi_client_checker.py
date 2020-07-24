import pyautogui
from time import sleep
import webbrowser
class jiofi:
    def __init__(self):
        pyautogui.hotkey("win","d")
        webbrowser.open_new("http://jiofi.local.html/")
        sleep(7)
        pyautogui.press('tab')
        pyautogui.press('enter')
        pyautogui.press('tab',4)
        pyautogui.typewrite('administrator')
        pyautogui.press('tab')
        pyautogui.typewrite('akashshiva123!')
        pyautogui.press('enter')
        sleep(3)
        pyautogui.press('tab',3)
        pyautogui.press('enter')        
        sleep(1)
        pyautogui.press('tab',8)
        pyautogui.press('enter')
        input()

if __name__ == "__main__":
    jio= jiofi()
