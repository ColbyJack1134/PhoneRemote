import requests
from pynput.keyboard import Key, Controller
from pynput.mouse import Button
import pynput
import os
import webbrowser

url = "[URL with command.txt]"
keyboard = Controller()
mouse = pynput.mouse.Controller()


def main():
    while True:
        #print(mouse.position)
        r = requests.get(url = url)
        if(len(r.text) != 0):
            print(r.text)
            if(r.text == "Pause"):
                pressKeyboard([Key.media_play_pause])
            elif(r.text == "Increase"):
                pressKeyboard([Key.media_volume_up])
            elif(r.text == "Decrease"):
                pressKeyboard([Key.media_volume_down])
            elif(r.text == "Mute"):
                pressKeyboard([Key.media_volume_mute])
            elif(r.text == "Space"):
                pressKeyboard([" "])
            elif(r.text == "Alt_Tab"):
                pressKeyboard([Key.alt, Key.tab])
            elif(r.text == "Alt_F4"):
                pressKeyboard([Key.alt, Key.f4])
            elif(r.text == "Brooklyn99"):
                webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s &").open("https://www.hulu.com/series/brooklyn-nine-nine-daf48b7a-6cd7-4ef6-b639-a4811ec95232")
            elif(r.text == "Ctrl_W"):
                pressKeyboard([Key.ctrl, "w"])
            elif(r.text == "Enter"):
                pressKeyboard([Key.enter])
            elif(r.text[:7] == "Google "):              
                webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito &").open("https://google.com/search?q="+r.text[7:])
            elif(r.text == "Mouse_1"):
                pressMouse([Button.left])
            elif(r.text == "Move_Mouse_Away"):  
                setMouse(0, 0)
            elif(r.text[:16] == "Move_Mouse_Left "):          #Added
                if(len(r.text) == 16):
                    moveMouse(-5, 0)
                else:
                    moveMouse(-1*int(r.text[16:]), 0)
            elif(r.text[:17] == "Move_Mouse_Right "):         #Added
                if(len(r.text) == 17):
                    mouse.move(5, 0)
                else:
                    moveMouse(int(r.text[17:]), 0)
            elif(r.text[:14] == "Move_Mouse_Up "):         #Added
                if(len(r.text) == 14):
                    mouse.move(0, -5)
                else:
                    moveMouse(0, -1*int(r.text[14:]))
            elif(r.text[:16] == "Move_Mouse_Down "):         #Added
                if(len(r.text) == 16):
                    mouse.move(0, 5)
                else:
                    moveMouse(0, int(r.text[16:]))
            elif(r.text[:19] == "Open_URL_Incogneto "):         
                webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito &").open(r.text[19:])
            elif(r.text[:9] == "Open_URL "):
                webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s &").open(r.text[9:])
            elif(r.text == "Shift_Tab"):
                pressKeyboard([Key.shift, Key.tab])
            elif(r.text == "Skip_Intro"):
                setMouse(1790, 950)
                pressMouse([Button.left])
            elif(r.text == "Tab"):
                pressKeyboard([Key.tab])
            elif(r.text == "Win_D"):
                pressKeyboard([Key.cmd_l, "d"])
            elif(r.text == "Win_Up"):
                pressKeyboard([Key.cmd_l, Key.up])
            elif(r.text == "Power Off"):
                os.system("shutdown /s /t 1")

            data = {'response':'Success!'}
            r = requests.post(url = "[URL with endpoint.php]", data = data)

def pressKeyboard(buttons):
    for i in buttons:
        keyboard.press(i)
    for i in buttons:
        keyboard.release(i)
def pressMouse(buttons):
    for i in buttons:
        mouse.press(i)
    for i in buttons:
        mouse.release(i)
def setMouse(x, y):
    mouse.position = (x, y)
def moveMouse(x, y):
    mouse.move(x, y)
        
while True:
    try:
        main()
    except KeyboardInterrupt:
        break
    except:
        print("ERROR")
        continue
        
    
