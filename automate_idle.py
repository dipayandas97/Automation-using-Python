import pyautogui as gui
import time
import numpy as np

while True:
    x = np.random.randint(500,900,1)[0]
    y = np.random.randint(300,650,1)[0]
    gui.click(x,y)
    wait = np.random.randint(1, 15, 1)
    time.sleep(wait)
    
