import os, sys, shelve

#########################################################
#Set script path and remove trailing \ if path is c:\
#########################################################
scriptPath = os.path.dirname(sys.argv[0])
if scriptPath[-1:]=='\\':
    scriptPath = scriptPath.strip('\\')
#########################################################
###################################################################
# PLAIN TEXT FILES - txt, py, csv, etc.
# other types of files are called 'binary files" - pdf, word, etc.
###################################################################

helloFile = open('{}\\hello.txt'.format(scriptPath))
textData = helloFile.read()
print(textData) # returns a single string
helloFile.close() # CAN NOT READ the same file twice!!!! must close are reopen
#...of course you could just read it and save data to a variable

for t in textData:  #we are looping through a string here, not a list
    #print(t) # this is a mess...it prints every letter in the string......
    continue

### a BETTER WAY
helloFile = open('{}\\hello.txt'.format(scriptPath))
lines = helloFile.readlines() #list of strings
print(lines)
helloFile.close() 
for l in lines:
    print(l) #weird part is that the NEWLINE char gets printed as its own line
    
for l in lines:
    print(l, end='')

#beware that the newline character was stripped away from the previous print statement
print("\nhello")

#PRINT FILES in FOLDER
files = os.listdir(scriptPath)

'''
opening a non-existant file in write or append mode will create the file

'''
#Print files with fullpath and write full paths to a text file - APPEND
helloFile = open('{}\\hello.txt'.format(scriptPath),'a') #open in append mode...do not overwrite existing
for f in files:
    print(os.path.join(scriptPath, f))
    helloFile.write(os.path.join(scriptPath, f) + '\n') #Need to add a newline here
helloFile.close()

#Print files with fullpath and write full paths to a text file - OVERWRITE!!
helloFile2 = open('{}\\hello2.txt'.format(scriptPath),'w') #open in write mode...will overwrite existing text
for f in files:
    print(os.path.join(scriptPath, f))
    helloFile2.write(os.path.join(scriptPath, f) + '\n') #Need to add a newline here
helloFile2.close()

#save binary data to self file -- import shelve
shelfFile = shelve.open('{}\\mydata'.format(scriptPath))
shelfFile['employees'] = ['Steez McQueez', 'Mr. CheesySneasel']
shelfFile['dict'] = {'firstName' : 'Steez', 'lastName' : 'McQueez'}
shelfFile['dict2'] = {'employees':[ {'firstName' : 'Steez', 'lastName' : 'McQueez'}, {'firstName' : 'Mr.', 'lastName' : 'CheesySneasel'}]}
shelfFile.close()
shelfFile = shelve.open('{}\\mydata'.format(scriptPath))
print(shelfFile['employees'][0])
print(shelfFile['dict']['firstName'])
print(shelfFile['dict2']['employees'][1]['lastName'])
print(shelfFile.keys())
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
print(type(list(shelfFile.values())))

#pritn the type for each shelfFile key and check if it is a dictionary
for i in list(shelfFile.values()):
    print(type(i))
    if type(i) is dict: # notice the use of the 'is' operator!
        print('It\'s a dict!!')

'''
Difference between == and is operator in Python. 
The == operator compares the values of both the operands and checks for value equality. 
Whereas is operator checks whether both the operands refer to the same object or not. ... 
We can check it with id() function in python which returns the “identity” of an object.
'''
