import pyautogui
import time
#Mode1=Shedu
#Mode2=Nataruk
#Mode3=Ignis/BeamWeapons with limited ammo
MODE=1
time.sleep(3)


if MODE == 1:
    while True:
      pyautogui.mouseDown();
      pyautogui.mouseDown(button='right')
   
elif MODE == 2:
    while True:
      pyautogui.mouseDown(button='right')
      pyautogui.mouseDown();
      time.sleep(.3)
      pyautogui.mouseUp();
      
      
elif MODE == 3:
    while True:
      pyautogui.mouseDown();
      

    

