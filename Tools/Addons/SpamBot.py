
import pyautogui 
import webbrowser as wb
import time
from tkinter import *

arayuz = Tk()
arayuz.title("SpamBotForChattingApps")
arayuz.geometry("550x300")
arayuz.minsize("550","300")
arayuz.maxsize("550","300")
arayuz.config(bg="#009900")


def spam():
    wb.open("web.whatsapp.com")
    time.sleep(30)
    for i in range(100000):
        pyautogui.press("s")
        pyautogui.press("p")
        pyautogui.press("a")
        pyautogui.press("m")
        pyautogui.press("enter")

startbutton = Button(arayuz,text="START",command=spam)
startbutton.pack()
startbutton.place(x=260,y=125)

uyarıcıtext = Label(text="UYARI:START TUŞUNA BASILDIKTAN 30SN SONRA SPAM ATMAYA BAŞLAR")
uyarıcıtext.pack()


arayuz.mainloop()