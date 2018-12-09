import json, csv, os

#variables
filePath1 = "C:/_Repositories/PythonTest/Data/test1.json"
filePath2 = "C:/_Repositories/PythonTest/Data/test2.json"
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

    jsonFile.close
    jsonFile2.close

    return

def main():
    update_json_data(filePath1)
    return

if __name__ == '__main__':
    globals()[sys.argv[1]]()