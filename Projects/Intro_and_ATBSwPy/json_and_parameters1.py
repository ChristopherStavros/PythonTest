import json, csv, sys

#variables
filePath1 = "C:/_Repositories/Python_Study/Data/test1.json"
filePath2 = "C:/_Repositories/Python_Study/Data/test2.json"
filePath3 = "C:/_Repositories/Python_Study/Data/test1.csv"
filePath4 = "C:/_Repositories/Python_Study/Data/employees.json"

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
    jsonFile.close()
    return fileData, lst



def combine_json(filePath1, filePath2):
    with open(filePath1, "r") as jsonFile:
        fileData = json.load(jsonFile)

    with open(filePath2, "r") as jsonFile2:
        fileData2 = json.load(jsonFile2)
    
    merged_dict2 = {**fileData, **fileData2}    

    print("Merged")
    print(merged_dict2)
    #print(type(merged_dict2))
    #print(type(merged_dict2["executives"]))
    #print(type(merged_dict2["executives"][1]))
    #print(type(merged_dict2["executives"][1]["ID"]))
    #print(merged_dict2["executives"][1])
    

def combine_data(filePath1, filePath2, filePath3):
    # get JSON data from files
    jsonFile = open(filePath1, "r+") #r+ means read and write
    fileData = json.load(jsonFile)
    jsonFile2 = open(filePath2, "r+")
    fileData2 = json.load(jsonFile2)

    # get data from csv and format for JSON
    with open(filePath3) as csvFile1:
        fileData3 = csv.DictReader(csvFile1)
        newList = []
        for dct in map(dict,fileData3):
            newList.append(dct)
    contractors = {"contractors":newList}

    # merge data
    merged_dict3 = {**fileData, **fileData2, **contractors}

    # write to JSON file
    with open(filePath4, 'w') as outfile:
        json.dump(merged_dict3, outfile, indent=4)

    # output message to screen
    print("The DATA has been combined")

    return  

def main():
    update_json_data(filePath1)
    return

#PARAMETERS
if len(sys.argv) == 2:
    command = sys.argv[1]
    if command == "combine_json":
        combine_json(filePath1, filePath2)
    if command == "combine_data":
        combine_data(filePath1, filePath2, filePath3)
else:
    #run the combine_json function if no parameters are passed to the script
    combine_json(filePath1, filePath2)

    
