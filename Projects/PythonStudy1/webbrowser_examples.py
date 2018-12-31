'''
Note to self:
Do not name files with the same name as a 'module'
THis will cause a script to become confused and look for functions within the script itself rather than within the module
...causing stuff like this

PS C:\_Repositories> python -u "c:\_Repositories\PythonTest\Projects\PythonStudy1\webbrowser.py"
Traceback (most recent call last):
  File "c:\_Repositories\PythonTest\Projects\PythonStudy1\webbrowser.py", line 1, in <module>
    import webbrowser, sys
  File "c:\_Repositories\PythonTest\Projects\PythonStudy1\webbrowser.py", line 3, in <module>
    webbrowser.open('https://www.automatetheboringstuff.com') #launches URL using default web browser
AttributeError: module 'webbrowser' has no attribute 'open'

'''

import webbrowser, sys, pyperclip

# #launches URL using default web browser
# will add a new tab if browser is already open
#webbrowser.open('https://www.automatetheboringstuff.com') 



#Check if command line arguments were passed
# ['webbrowser_examples.py', '870', 'Valencia', 'St.'
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:]) #start slice at index 1 and join arguments into a single string value 
    #with a single space in between them
else:
     #address = "870 Valencia St."
     address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
