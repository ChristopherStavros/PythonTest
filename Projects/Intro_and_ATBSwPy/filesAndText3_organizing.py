import shutil
import os, sys # for scriptPath var
import send2trash #must be installed with pip

#########################################################
#Set script path and remove trailing \ if path is c:\
#########################################################
scriptPath = os.path.dirname(sys.argv[0])
if scriptPath[-1:]=='\\':
    scriptPath = scriptPath.strip('\\')
#########################################################

#copy a file shutil.copy(sourceFile, destination)  
if os.path.exists('{}\\hello2.txt'.format(scriptPath)):
    shutil.copy('{}\\hello2.txt'.format(scriptPath), 'c:\\temp')

#specify new name in destination area to rename
if os.path.exists('{}\\hello2.txt'.format(scriptPath)):
    shutil.copy('{}\\hello2.txt'.format(scriptPath), 'c:\\temp\\renamedHello2.txt')

#copy entire folder - does not overwrite!!!! will throw an error
if not os.path.exists('c:\\temp\\new'):    
    shutil.copytree('c:\\temp', 'c:\\temp\\new')
else:
    print('c:\\temp\\new' + ' already exists')

#move or rename
if os.path.exists('{}\\hello2.txt'.format(scriptPath)):
    shutil.move('{}\\hello2.txt'.format(scriptPath), '{}\\testFile.txt'.format(scriptPath))
else:
    print('The file does not exist')

#makeDir 
if not os.path.exists('{}\\testDir'.format(scriptPath)):
    os.mkdir('{}\\testDir'.format(scriptPath))
else:
    print('The dir already exist')

#################################
# deleting - PERMANENT DELETE
#################################

#remove file
if os.path.exists('{}\\testFile.txt'.format(scriptPath)):
    os.unlink('{}\\testFile.txt'.format(scriptPath)) #will not send to recycle bin 
    #will permanently delete - same as shutil.mtree()

#os.rmdir - must be empty
#shutil.rmtree() - will delete all files and folders in tree 
# ....and WILL NOT SEND THEM TO RECYCLE BIN!!!!!!
'''
if os.path.exists('{}\\testDir'.format(scriptPath)):
    try:
        os.rmdir('{}\\testDir'.format(scriptPath)) # must be an empty dir 
    except OSError:
        print("An OS error has occurred, running rmtree()")
        shutil.rmtree('{}\\testDir'.format(scriptPath))
else:
    print('The dir does not exist)')
'''
    

#######################################
# deleting - using send2trash module
#this is a better way
'''
pip install send2trash
'''
#######################################
send2trash.send2trash('{}\\testDir'.format(scriptPath)) # works on files or folders (empty or not)
