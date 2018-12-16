import json, csv, os

#variables
filePath1 = "C:/_Repositories/PythonTest/Data/test1.json"
filePath2 = "C:/_Repositories/PythonTest/Data/test2.json"
filePath3 = "C:/_Repositories/PythonTest/Data/test1.csv"

###########
# functions
###########

def update_json_data(filePath1):
    jsonFile = open(filePath1, "r+")
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

    ###########
    # output
    ###########

    #print list derived from json data
    #print("List derived from json data")
    #print(lst)

    #print 'Key'
    #print("Employees key")
    #print(fileData["employees"])

    #print pure json
    #print("Pure json data")
    #print(fileData)
    #cleanup
    jsonFile.close
    return fileData, lst



def combine_json(filePath1, filePath2):
    jsonFile = open(filePath1, "r+")
    fileData = json.load(jsonFile)

    jsonFile2 = open(filePath2, "r+")
    fileData2 = json.load(jsonFile2)
    merged_dict2 = {**fileData, **fileData2}    

    print("Merged")
    print(merged_dict2)
    print(type(merged_dict2))
    print(type(merged_dict2["executives"]))
    print(type(merged_dict2["executives"][1]))
    print(type(merged_dict2["executives"][1]["ID"]))
    print(merged_dict2["executives"][1])

    jsonFile.close
    jsonFile2.close

    return

def combine_data(filePath1, filePath2, filePath3):
    jsonFile = open(filePath1, "r+")
    fileData = json.load(jsonFile)

    jsonFile2 = open(filePath2, "r+")
    fileData2 = json.load(jsonFile2)

    csvFile1 = open(filePath3)
    fileData3 = csv.DictReader(csvFile1)
    print(type(fileData3))
    
    newDict = {}
    for row in fileData3:
       newDict.update(dict(row))

    contractors = {"contractors":[newDict]}


    print(newDict)
    print(type(newDict))

    merged_dict3 = {**fileData, **fileData2, **contractors}  
    print(merged_dict3)
    return  

def main():
    update_json_data(filePath1)
    return

if __name__ == '__main__':
    from sys import argv
    command = argv[1]
    if command == "combine_json":
        combine_json(filePath1, filePath2)
    if command == "combine_data":
        combine_data(filePath1, filePath2, filePath3)

    
