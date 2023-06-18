import time
import pyautogui 

print("""

#########   #########  #########   #           ###########
    #       #       #  #       #   #           #
    #       #       #  #       #   #           #
    #       #       #  #       #   #           ###########
    #       #       #  #       #   #                     #
    #       #########  #########    ########   ###########

""")

print("1]Start")

print("2]Help")

print("C^]Exit")


wait = 0
Wait = input()

#HELP

if Wait == "2" :
  print("""
 THANKS FOR DOWNLOADING MY TOOL MENU
 Version 1.0
 
 News:
 ...
 
 V.1.1 coming soon:
 Zphisher
 Banners
 new tools
 hqlmap
 and more...
 
 
 RESTART PLEASE
 """)




#START 
if Wait == "1" :
  print("""
  
  -----------------SELECT-------------------
  | 1]SpamBot                              |
  |                                        |
  |                                        |                
  |                                        |
  |                                        |
  |                                        |
  |                                        |
  |                                        |
  |                                        |
  |                                        |
  |                                        |
  |                                        |
  ------------------------------------------
  
  """)

Select = input()
  
if Select == "1" :
 print("SPAMBOT")
 
 print("1]Start SpamBOT")
 
 spambot = input()
 
 if spambot == "1" :
    print("Wait 10 second")
    time.sleep(10)
    for i in range(100000):
        pyautogui.press("s")
        pyautogui.press("p")
        pyautogui.press("a")
        pyautogui.press("m")
        pyautogui.press("enter")

  