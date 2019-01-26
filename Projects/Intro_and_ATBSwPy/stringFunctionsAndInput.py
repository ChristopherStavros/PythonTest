'''
python -m pip install --upgrade pip
pip install pyperclip
'''

import random
import pprint
import pyperclip

#get input from console
var = input()

#some string functions
var2 = "****Hell**ooo****".strip('*Ho')
print(var2)
print("hello".replace("e", "3"))

#print value recieve from consol input and covert it to upper case
print(var.upper())

#get input, print and covert in one line
#because I added the 'end' statement this line will not add the \n to the end..which is the default...
#so I added \n to the end
print(input().lower(), var, random.randint(1,3333), var2, sep="....", end="....and that's all folks.\n")

#using piperclip, print whatever is on the clipboard to the screen
var = pyperclip.paste()
print(var)
print(var)

#String formatting using "Conversion specifiers"
print('Hello, %s, Welcome to %s!' % ('Christopher', 'The Jungle'))