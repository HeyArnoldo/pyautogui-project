import pyautogui as pa
import time
import keyboard
import win32api,win32con

#-----------[ CONFIG ]-----------
timeSleep = 0.017
TimeSleepSwitch1= 0.01
TimeSleepSwitch2= 0.01

useKey = "ctrl+r"
exitKey = "ctrl+z"

cascoKey = 3 #Only Number
pecheraKey = 4 #Only Number
pantalonKey = 5 #Only Number
botasKey = 6 #Only Number
#-----------[ CONFIG ]-----------

FullHDConfig = (815,405)
HDConfig = (545,250)
resolutionWindow=pa.size()
if resolutionWindow == (1920,1080) :
    xposCasco = FullHDConfig[0]
    yposCasco = FullHDConfig[1]
else :
    xposCasco = HDConfig[0]
    yposCasco = HDConfig[1]

def pressButton(key):
    time.sleep(timeSleep)
    key=key+48
    win32api.keybd_event(key,0,0,0)
    time.sleep(timeSleep)
    win32api.keybd_event(key,0,win32con.KEYEVENTF_KEYUP,0)

def pressButtonE():
    timeSleep = 0.01
    win32api.keybd_event(69,0,0,0)
    time.sleep(timeSleep)
    win32api.keybd_event(69,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(timeSleep) 

def switch1() :
    timeSleep = TimeSleepSwitch1
    time.sleep(timeSleep)

    win32api.SetCursorPos((xposCasco,yposCasco+145))
    time.sleep(timeSleep)
    pressButton(cascoKey)

    win32api.SetCursorPos((xposCasco+35,yposCasco+145))
    time.sleep(timeSleep)
    pressButton(pecheraKey)

    win32api.SetCursorPos((xposCasco,yposCasco+180))
    time.sleep(timeSleep)
    pressButton(pantalonKey)

    win32api.SetCursorPos((xposCasco+35,yposCasco+180))
    time.sleep(timeSleep)
    pressButton(botasKey)

def switch2() :
    timeSleep = TimeSleepSwitch2

    win32api.SetCursorPos((xposCasco,yposCasco))
    time.sleep(timeSleep)
    pressButton(cascoKey)

    win32api.SetCursorPos((xposCasco,yposCasco+35))
    time.sleep(timeSleep)
    pressButton(pecheraKey)

    win32api.SetCursorPos((xposCasco,yposCasco+70))
    time.sleep(timeSleep)
    pressButton(pantalonKey)

    win32api.SetCursorPos((xposCasco,yposCasco+105))
    time.sleep(timeSleep)
    pressButton(botasKey)

def switch2legitv1():
    time.sleep(timeSleep)

    pa.moveTo(x=xposCasco,y=yposCasco)
    pa.press(str(cascoKey),_pause=True)
    time.sleep(timeSleep)
    pa.moveTo(x=xposCasco,y=yposCasco+35)
    pa.press(str(pecheraKey),_pause=True)
    time.sleep(timeSleep)
    pa.moveTo(x=xposCasco,y=yposCasco+70)
    pa.press(str(pantalonKey),_pause=True)
    time.sleep(timeSleep)
    pa.moveTo(x=xposCasco,y=yposCasco+105)
    pa.press(str(botasKey),_pause=True)
    time.sleep(timeSleep)

def switch2legitv2():
    time.sleep(timeSleep)

    pa.moveTo(x=xposCasco,y=yposCasco)
    pa.press(str(cascoKey))
    pa.moveTo(x=xposCasco,y=yposCasco+35)
    pa.press(str(pecheraKey))
    pa.moveTo(x=xposCasco,y=yposCasco+70)
    pa.press(str(pantalonKey))
    pa.moveTo(x=xposCasco,y=yposCasco+105)
    pa.press(str(botasKey))

while True:
        x, y = pa.position()
        if keyboard.is_pressed(useKey):
            t1 = time.time()

            pressButtonE()
            time.sleep(timeSleep)
            switch1()
            time.sleep(timeSleep)
            switch2()
            
            #switch2legitv2()
            #switch2legitv1()
            time.sleep(timeSleep)
            switch1()
            time.sleep(timeSleep)
            pressButtonE()

            time.sleep(timeSleep)
            t2 = time.time()
            print("Switch in: ",t2-t1)
        if keyboard.is_pressed(exitKey):
            break