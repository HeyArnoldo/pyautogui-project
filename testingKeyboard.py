import pyautogui as pa
import time
import keyboard

useFullHD = False
timeSleep = 0.017

cascoKey = "3"
pecheraKey = "4"
pantalonKey = "5"
botasKey = "6"

useKey = "x"
exitKey = "z"



FullHDConfig = (815,405)
HDConfig = (545,250)
if useFullHD :
    xposCasco = FullHDConfig[0]
    yposCasco = FullHDConfig[1]
else :
    xposCasco = HDConfig[0]
    yposCasco = HDConfig[1]

while True:
        x, y = pa.position()
        if keyboard.is_pressed(useKey):
            pa.press("e")

            pa.moveTo(x=xposCasco,y=yposCasco+145,_pause=True)
            pa.press(cascoKey,_pause=False)
            time.sleep(timeSleep)
            pa.moveTo(x=xposCasco+35,y=yposCasco+145)
            pa.press(pecheraKey,_pause=False)
            time.sleep(timeSleep)
            pa.moveTo(x=xposCasco,y=yposCasco+180)
            pa.press(pantalonKey,_pause=False)
            time.sleep(timeSleep)
            pa.moveTo(x=xposCasco+35,y=yposCasco+180)
            pa.press(botasKey,_pause=False)
            time.sleep(timeSleep)

            pa.moveTo(x=xposCasco,y=yposCasco)
            pa.press(cascoKey,_pause=False)
            time.sleep(timeSleep)
            pa.moveTo(x=xposCasco,y=yposCasco+35)
            pa.press(pecheraKey,_pause=False)
            time.sleep(timeSleep)
            pa.moveTo(x=xposCasco,y=yposCasco+70)
            pa.press(pantalonKey,_pause=False)
            time.sleep(timeSleep)
            pa.moveTo(x=xposCasco,y=yposCasco+105)
            pa.press(botasKey,_pause=False)
            time.sleep(timeSleep)

            pa.moveTo(x=xposCasco,y=yposCasco+145,_pause=True)
            pa.press(cascoKey,_pause=False)
            time.sleep(timeSleep)
            pa.moveTo(x=xposCasco+35,y=yposCasco+145)
            pa.press(pecheraKey,_pause=False)
            time.sleep(timeSleep)
            pa.moveTo(x=xposCasco,y=yposCasco+180)
            pa.press(pantalonKey,_pause=False)
            time.sleep(timeSleep)
            pa.moveTo(x=xposCasco+35,y=yposCasco+180)
            pa.press(botasKey,_pause=False)
            time.sleep(timeSleep)

            pa.press("e")
        if keyboard.is_pressed(exitKey):
            break