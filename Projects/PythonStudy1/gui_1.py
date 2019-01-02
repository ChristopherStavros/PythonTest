'''
https://pyautogui.readthedocs.io/en/latest/

pip install pyautogui

FAILSAFE
To avoid disaster - SLAM THE MOUSE INTO THE TOP LEFT CORNER

pyautogui.FailSafeException: PyAutoGUI fail-safe triggered from mouse moving to upper-left corner. 
To disable this fail-safe, set pyautogui.FAILSAFE to False.


ALSO COOL - FROM TERMINAL ONLY

PS C:\_Repositories> py
Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import pyautogui
>>> pyautogui.displayMousePosition()
Press Ctrl-C to quit.
X:  446 Y:  795 RGB: ( 30,  30,  30)

'''
import pyautogui

print(pyautogui.size())
width, height = pyautogui.size()  #Screen resolution
print(width)
print(height)
print(pyautogui.position()) #current mouse position

pyautogui.moveTo(1200, 500, duration=1.5) #move mouse!!!

pyautogui.moveRel(-200, 0) #move -200 left...can also add a duration if wanted, otherwise it will be immediate

pyautogui.click(339, 30) #click somewhere...this opens the VScode debug menu for me :)

'''
also

.rightClick()
.leftClick()
.dragRight()
.dragLeft()
'''


