from PIL import ImageGrab
import os
# os.environ['DISPLAY'] = ':1'
import pyautogui
import PIL
import time

pyautogui.hotkey('alt', 'tab')

while True:
    pyautogui.press('tab', 10, 0.2)