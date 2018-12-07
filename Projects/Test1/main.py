import json
import csv
import os

f = open("E:/Files/Docs/GitHub/PythonTest/Data/test1.json")
lst = []
fileData = json.load(f)
#print("Employees")
#print(fileData["employees"])

for key in fileData:
    print(key)
    #lst.append(fileData[key])
    for e in fileData[key]:
        print(e)
        print(e["firstN ame"])

    #lst.append(temp)

#print(lst)

#print(fileData)



