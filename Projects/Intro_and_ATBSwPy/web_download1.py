'''
pip install requests
https://requests.readthedocs.io/en/master/
Requests module is only good if you know the exact URL needed for the download
'''
import requests
import os, sys
#########################################################
#Set script path and remove trailing \ if path is c:\
#########################################################
scriptPath = os.path.dirname(sys.argv[0])
if scriptPath[-1:]=='\\':
    scriptPath = scriptPath.strip('\\')
#########################################################

#get file and save it in variable --> res
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

#print status code
print(res.status_code) #200 is GOOD
#lenth of text
print(len(res.text))
#print the first 500 characters --- using a slice
print(res.text[:500])
#raise exception if bad download occurs
res.raise_for_status()
#BAD REQUEST
badRes = requests.get('https://automatetheboringstuff.com/files/rzzzzzz.txt')
#raise exception if bad download occurs
#badRes.raise_for_status()

#DOWNLOAD FILE!
playfile = open('%s\\rj.txt' % (scriptPath), 'wb') # open file in wb --- write-binary mode
for chunk in res.iter_content(100000):  # specify number of bytes per chunk
    playfile.write(chunk)

playfile.close()

####EXTRA
#r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
#print(r.json())