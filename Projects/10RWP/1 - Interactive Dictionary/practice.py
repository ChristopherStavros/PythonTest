from c_utils import *
import json
import os

# Get json from file
def from_json(file):
    with open(file, 'r') as f:
        return json.load(f)

# Get definition
def get_def(word):
    word = word.lower()
    if word in data:
        return data[word]

# Pull in list of json files from script path
# testfiles = ["{}/{}".format(script_path, f) for f in os.listdir(script_path) if f[-5:]== '.json']
testfiles = ["{}/{}".format(script_path, f) for f in os.listdir(script_path) if '.json' in f]
print(testfiles)

# Iterate through JSON files and load them
maps = map(from_json, testfiles)

# Unpack values and combine into a single dictionary
data = {}
for m in maps:
    data = {**data, **m}

# OUTPUT
word = input("Enter word: ")
print(get_def(word))