import keyboard
import pyautogui as pa
import random
import time
import mouse
#HeyArnoldo´s Size = Size(width=1366, height=768)
xposCasco = 545
yposCasco = 250

cascoKey = "3"
pecheraKey = "4"
pantalonKey = "5"
botasKey = "6"

delay = "0.05"

while True:
        x, y = pa.position()
        if keyboard.is_pressed("x"):
            pa.moveTo()

            pa.moveTo(x=xposCasco,y=yposCasco+145)
            pa.press(cascoKey)
            pa.moveTo(x=xposCasco+35,y=yposCasco+145)
            pa.press(pecheraKey)
            pa.moveTo(x=xposCasco,y=yposCasco+180)
            pa.press(pantalonKey)
            pa.moveTo(x=xposCasco+35,y=yposCasco+180)
            pa.press(botasKey)

            pa.moveTo(x=xposCasco,y=yposCasco)
            pa.press(cascoKey)
            pa.moveTo(x=xposCasco,y=yposCasco+35)
            pa.press(pecheraKey)
            pa.moveTo(x=xposCasco,y=yposCasco+70)
            pa.press(pantalonKey)
            pa.moveTo(x=xposCasco,y=yposCasco+105)
            pa.press(botasKey)

            pa.moveTo(x=xposCasco,y=yposCasco+145)
            pa.press(cascoKey)
            pa.moveTo(x=xposCasco+35,y=yposCasco+145)
            pa.press(pecheraKey)
            pa.moveTo(x=xposCasco,y=yposCasco+180)
            pa.press(pantalonKey)
            pa.moveTo(x=xposCasco+35,y=yposCasco+180)
            pa.press(botasKey)

        if keyboard.is_pressed("z"):
            break