import time
import pyautogui 
import os
os.system("")

COLOR = {
    "HEADER": "\033[95m",
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "RED": "\033[91m",
    "ENDC": "\033[0m",
}

print(COLOR["GREEN"],"""


#########   #########  #########   #           ###########
    #       #       #  #       #   #           #
    #       #       #  #       #   #           #
    #       #       #  #       #   #           ###########
    #       #       #  #       #   #                     #
    #       #########  #########    ########   ###########


""", COLOR["ENDC"])


print(COLOR["RED"],"1]Start", COLOR["ENDC"])

print(COLOR["RED"],"2]Help", COLOR["ENDC"])

print(COLOR["RED"],"C^]Exit", COLOR["ENDC"])


wait = 0
Wait = input()

#HELP

if Wait == "2" :
  print("""
  # Termux-Tools

 This is version 1.1

 if you like version 1.1 wait big update

 TERMUX TOOLS:
 SpamBOT
 ipinfo
 midipianoplayer
 
 coming soon:
 zphisher
 sqlmap
 wifite
 wifite 2
 ...
 and more
 
 
 RESTART PLEASE
 """)




#START 
if Wait == "1" :
  print(COLOR["GREEN"],"""
  
  
    
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
  
  """, COLOR["ENDC"])
 

Select = input()
  
if Select == "1" :
 print(COLOR["RED"],"SPAM BOT", COLOR["ENDC"])
 
 print(COLOR["RED"],"1]Start", COLOR["ENDC"])
 print(COLOR["RED"],"C^]Exit", COLOR["ENDC"])
 
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

  