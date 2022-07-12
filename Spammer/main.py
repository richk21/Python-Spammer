import pyautogui
import time

crash = open("crasher.txt", "r")
crasher = crash.read()
pack = input("How many packets? : ")
time.sleep(2)
for i in range(int(pack)):
    pyautogui.typewrite(crasher)
    pyautogui.press("enter")
    time.sleep(1)
