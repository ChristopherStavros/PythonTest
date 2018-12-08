import json, csv, os

jsonFile = open("E:/Files/Docs/GitHub/PythonTest/Data/test1.json", "r+")
lst = []
fileData = json.load(jsonFile)
#print("Employees")
#print(fileData["employees"])

for key in fileData:
    for record in fileData[key]:
        if(record["firstName"]=="Steez" and record["lastName"]=="McQueez"):
            record["species"] = "strigoi"
        else:
            record["species"] = "vampire"
        lst.append(record)
         
jsonFile.seek(0)
json.dump(fileData, jsonFile, indent=4)
jsonFile.truncate()

jsonFile.close

#print list derived from json data
print(lst)

#print pure json
print(fileData)
