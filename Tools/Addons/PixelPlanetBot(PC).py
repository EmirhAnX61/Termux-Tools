import pyautogui as pag
import pyautogui
import random
import time


while True:
    x = random.randint(600,700)
    y = random.randint(200,600)
    pag.moveTo(x,y,0.5)
    pyautogui.press("Left_Click")
    time.sleep(5)

