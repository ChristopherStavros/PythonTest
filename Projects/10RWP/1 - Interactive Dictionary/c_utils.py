import os, sys, json

'''variables'''
script_path = os.path.dirname(sys.argv[0])
if script_path[-1:]=='\\':
    script_path = script_path.strip('\\')

'''functions'''
def dir(folder):
    for foldername, subfolder, filenames in os.walk(folder):
        for file in filenames:
            print(os.path.join(foldername, file)) # dir or Get-ChildItem style return :)

# Get json from file
def from_json(file):
    with open(file, 'r') as f:
        return json.load(f)