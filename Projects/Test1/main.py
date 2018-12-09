import json, csv, os

#variables
jsonFile = open("E:/Files/Docs/GitHub/PythonTest/Data/test1.json", "r+")
lst = []
fileData = json.load(jsonFile)

#main loop
for key in fileData:
    for record in fileData[key]:
        if(record["firstName"]=="Steez" and record["lastName"]=="McQueez"):
            record["species"] = "strigoi"
        else:
            record["species"] = "vampire"
        lst.append(record)

#write to json file       
jsonFile.seek(0)
json.dump(fileData, jsonFile, indent=4)
jsonFile.truncate()

#cleanup
jsonFile.close

###########
# output
###########

#print list derived from json data
print("List derived from json data")
print(lst)

#print 'Key'
print("Employees key")
print(fileData["employees"])

#print pure json
print("Pure json data")
print(fileData)
