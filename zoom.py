#program to automate zoom app

import subprocess
import pyautogui
import time

time_table={"Monday" : [ ,"OS" : ""]}
subprocess.Popen([r'C:\Users\akash\AppData\Roaming\Zoom\bin\Zoom.exe'])
print(pyautogui.position())
time.sleep(1)
pyautogui.click(956,506)
req_word="Tuesday"
fhand = open("time_table.txt","r")
for word in fhand:
    word - word.strip()
    if word == req_word:
        print("found")
    
