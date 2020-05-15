# Add this file to 'Custom Keyboard shortcut', to launch this file automatically on a certain keyboard shortcut
# Modify address_bar_x, address_bar_y according to your screen and browser dimensions
# Modify filepath to your desired download location

import pyautogui as gui
import pafy
import clipboard as cb
import time

filepath = '/home/dipayan/Downloads/my_music/'

#pre-requisite : web-browser has to be in maximized mode
address_bar_x, address_bar_y = 400, 115 #for my screen size and mozilla

#click on address bar
gui.click(0,440)                        #reset brownser state
gui.click(address_bar_x, address_bar_y) #click to select url

#copy address to clip-board
gui.hotkey('ctrl', 'c')
time.sleep(.1)  

#get address from clip-board
url = cb.paste()

video = pafy.new(url)
try:
    best_audio = video.getbestaudio()
    tmp = best_audio.download(filepath=filepath, quiet=True)
    gui.alert('File Download Complete !')

except:
    gui.alert('No audio format available for this URL')



