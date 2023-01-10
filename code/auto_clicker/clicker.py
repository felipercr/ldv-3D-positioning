import pyautogui as pag
import time

# auto_clicker/imgs/acquire.png

button = 'acquire.png'

def acquire(last):

    location = None
    while location == None: location = pag.locateCenterOnScreen(f'auto_clicker/imgs/{button}', confidence=0.7)

    pag.click(location)

    time.sleep(0.2)    

    if last == True: return

    location = None
    while location == None: location = pag.locateCenterOnScreen(f'auto_clicker/imgs/{button}', confidence=0.7)

    return
