import os, sys
#########################################################
#Set script path and remove trailing \ if path is c:\
#########################################################
scriptPath = os.path.dirname(sys.argv[0])
if scriptPath[-1:]=='\\':
    scriptPath = scriptPath.strip('\\')
#########################################################

#Try/Except
try:
    num = 42/0
except ZeroDivisionError:
    print("1: You divided by zero")

try:
    #raise Exception('This is the error message')
    raise ZeroDivisionError('You did it, divided by zero') #raising an exception
except ZeroDivisionError:
    print('Not good :  You divided by zero')
except:
    print('It happened :  A generic error')

#crashes the program
#raise ZeroDivisionError('You did it, divided by zero') #raising an exception

def boxPrint(symbol, width, height):
    #Raise exception if len(symbol) is greater than 1
    #...to prevent a weird shaped box
    if len(symbol) !=1:
        raise Exception('"Symbol" needs to be a string of length 1')
    #Raise exception if width or height are less than 2
    if (width < 2) or (height < 2):
        raise Exception('"Width" and "Height" must be greater or equal to 2')

    #Top of the box
    print(symbol * width)
    #Side and open middle of the box
    for i in range(height-2):
        print(symbol + (' ' * (width -2)) + symbol)
        #start with the symbol for the lft side of the box
        #then create width-2 blank spaces
        #...(-2 to account to the symbol on each side of the box) 
        #then add symbol for the right side of the box
    #Bottom of the box
    print(symbol * width)

boxPrint('*', 15, 5)
#This will product a weird shape..unless exception is raised
#boxPrint('**', 15, 5)
#boxPrint('*', 1, 2)

'''
TRACEBACK -->  error message
---callstack

traceback.format_exc()
import traceback
'''
import traceback
try:
    raise Exception('This is the error message')
except:
    errorFile = open('{}\\error_log.txt'.format(scriptPath), 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorlog.txt')

