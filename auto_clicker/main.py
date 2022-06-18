import pyautogui as pag
import time

time.sleep(2)
location = pag.locateOnScreen('imgs/num_9.png')
while location == None: location = pag.locateOnScreen('imgs/num_9.png')

pag.click('imgs/num_9.png')

