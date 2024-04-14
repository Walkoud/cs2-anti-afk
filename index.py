from pynput import keyboard
from pynput.keyboard import Controller
import time
import sys
import threading

keyboard1 = Controller()

print('''

 █████  ███    ██ ████████ ██        █████  ███████ ██   ██      ██████ ███████ ██████  
██   ██ ████   ██    ██    ██       ██   ██ ██      ██  ██      ██      ██           ██ 
███████ ██ ██  ██    ██    ██ █████ ███████ █████   █████       ██      ███████  █████  
██   ██ ██  ██ ██    ██    ██       ██   ██ ██      ██  ██      ██           ██ ██      
██   ██ ██   ████    ██    ██       ██   ██ ██      ██   ██      ██████ ███████ ███████ 
                                                                                        
                                                                            by Walkoud



Type "m" to activate anti-afk or desactivate
Type "!" to exit
''')

active = False
running = True

def on_key_release(key):
    global active, running
    #print('Released Key %s' % key)

    if str(key) == "'m'":
        if active:
            active = False
            print("ANTI-AFK desactivated - OFF")
            keyboard1.release('g')
            keyboard1.release('a')
            keyboard1.release('w')
            keyboard1.release('z')
            keyboard1.release('d')
        else:
            active = True
            print("ANTI-AFK activated - ON")

            
    if str(key) == "'!'":
        running = False

def anti_afk():
    while running:
        time.sleep(1)
        if active == True:
            keyboard1.press("w")
            keyboard1.press("z")
            time.sleep(1)
            keyboard1.release('w')
            keyboard1.release('z')
            keyboard1.press("d")
            time.sleep(1)
            keyboard1.release('d')
            keyboard1.press("g")
            keyboard1.press("a")
            time.sleep(1)
            keyboard1.release('g')
            keyboard1.release('a')
            
           

listener = keyboard.Listener(on_release=on_key_release)
listener.start()

anti_afk_thread = threading.Thread(target=anti_afk)
anti_afk_thread.start()

anti_afk_thread.join()

listener.stop()

