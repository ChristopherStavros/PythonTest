'''
PART3

https://pyautogui.readthedocs.io/en/latest/
pip install pyautogui

https://github.com/asweigart/sushigoroundbot


'''
import pyautogui

'''
IMAGE RECOGNITION!!
PILLOW IMAGING MODULE - CHAPTER 17!!!!
'''
import os, sys
#########################################################
#Set script path and remove trailing \ if path is c:\
#########################################################
scriptPath = os.path.dirname(sys.argv[0])
if scriptPath[-1:]=='\\':
    scriptPath = scriptPath.strip('\\')
#########################################################
os.chdir(scriptPath)
print(os.getcwd())
#########################################################
screenshot = '%s\\Example_Files\\screenshot_example.png' % (scriptPath)
pyautogui.screenshot(screenshot)
print(pyautogui.locateOnScreen(screenshot)) # if found will return tuple (34 , 45, 200, 455) for location...or None if not found 

print(pyautogui.locateCenterOnScreen(screenshot)) 

#move to location of image
pyautogui.moveTo(pyautogui.locateCenterOnScreen(screenshot))