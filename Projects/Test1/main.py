import json
import csv
import os

f = open("E:/Files/Docs/GitHub/PythonTest/Data/test1.json", "r+")
lst = []
fileData = json.load(f)
#print("Employees")
#print(fileData["employees"])

for key in fileData:
    for e in fileData[key]:
        #print(e)
        #print(e["ID"])
        if(e["firstName"]=="Steez" and e["lastName"]=="McQueez"):
            e["species"] = "strigoi"
        else:
            e["species"] = "vampire"
        lst.append(e)
         
f.seek(0)
json.dump(fileData, f, indent=4)
f.truncate()

f.close

#print list derived from json data
print(lst)

#print pure json
print(fileData)
