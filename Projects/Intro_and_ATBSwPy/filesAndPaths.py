import os, sys

'''
Python will base relative paths off of cwd ---> os.getcwd()
'''
#Get current working directory
currentWorkingDirectory = os.getcwd()
print(currentWorkingDirectory)

#########################################################
#Set script path and remove trailing \ if path is c:\
#########################################################
scriptPath = os.path.dirname(sys.argv[0])
if scriptPath[-1:]=='\\':
    scriptPath = scriptPath.strip('\\')
#########################################################

#change dir to scriptpath
os.chdir(scriptPath)

#Get current working directory
currentWorkingDirectory = os.getcwd()
print(currentWorkingDirectory)

#print absolute path of a.wav
print(os.path.abspath('a.wav'))
print(os.path.abspath('..\\..\\..\\..')) # c:\
print(os.path.abspath('c:\\')) # c:\

#is absolute path?
print(os.path.isabs('a.wav')) # false
print(os.path.isabs(os.path.abspath('a.wav')))  #true

#get path relatuve to another path
print(os.path.relpath(scriptPath, 'c:\\_Repositories'))

#the 0 is optional
song = "{0}\\a.wav".format(scriptPath)
print(song)
#base dir
print(os.path.dirname(song))
#strip away path and only include filename
print(os.path.basename(song))

#TEST for PATH
print(os.path.exists(scriptPath))
#TEST if dir
print(os.path.isdir(scriptPath))
#TEST if file
print(os.path.isfile(scriptPath))

#GET SIZE
print(os.path.getsize(scriptPath)) #get size of folder only, not files contained within
print(os.path.getsize(song)) #get size of file

#PRINT FILES in FOLDER
files = os.listdir(scriptPath)
print(files)

#Print files with fullpath
for f in files:
    print(os.path.join(scriptPath, f))

#play song
#os.system(song)

#Get size of all files in a folder
totalSize = 0
for filename in os.listdir(scriptPath):
    if not os.path.isfile(os.path.join(scriptPath, filename)):   #JOIN path and file name
        continue
    totalSize += os.path.getsize(os.path.join(scriptPath, filename))
print(totalSize)

#Make new folders if they do not already exist
newFolders = '{}\\WALNUT\\WAFFLES'.format(scriptPath)
if not os.path.exists(newFolders):
    os.makedirs(newFolders)
