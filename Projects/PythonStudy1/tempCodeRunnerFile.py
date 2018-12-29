
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