import os, sys

#########################################################
#Set script path and remove trailing \ if path is c:\
#########################################################
scriptPath = os.path.dirname(sys.argv[0])
if scriptPath[-1:]=='\\':
    scriptPath = scriptPath.strip('\\')
#########################################################

#this only gets the next level down
for item in os.listdir("c:\\_Repositories"):
    print(item)

'''
#this is junk!

for item in os.walk("c:\\_Repositories"):
    for i in item:
        print(i)

#basically same result as above

for foldername, subfolders, filenames in os.walk(scriptPath):
    print(foldername)
    print(subfolders)
    print(filenames)
'''
for foldername, subfolders, filenames in os.walk(scriptPath):
    for file in filenames:
        print(os.path.join(foldername, file)) # dir or Get-ChildItem style return :)
    
    print('The folder is ' + foldername)
    print('The subfolders in ' + foldername + ' are: ' + str(subfolders)) # convert list value to string
    print('The filenames in ' + foldername + ' are: ' + str(filenames)) # convert list value to string
    print()
    '''
    for subfolder in subfolders:
        print(subfolder + " : hello")
    for file in filenames:
        if file.endswith('.py'):
            print(file + ' : THis is a python file!')
    '''
    
    