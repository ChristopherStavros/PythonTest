'''
PART2...

https://pyautogui.readthedocs.io/en/latest/
pip install pyautogui

https://github.com/asweigart/sushigoroundbot


'''
import pyautogui

#KEYBOARD!!! notice the two commands on one line, in sequence
pyautogui.click(470,700); pyautogui.typewrite("Hello world", interval=0.2) # interval is optional
pyautogui.typewrite(['a','b', 'left', 'X', 'Y'], interval=0.2) # interval is optional

print(pyautogui.KEYBOARD_KEYS)
print(pyautogui.KEY_NAMES)

pyautogui.hotkey('win', 'e')
pyautogui.press('win')

