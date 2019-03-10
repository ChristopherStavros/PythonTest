import requests
from  simplejson.errors import JSONDecodeError
from createExceptions import APIThrottleLimitError

# number = input("Enter a number: ")
# try:
#     print(int(number) * 2)
# except LookupError:
#     print('Lookup error? This should never happen...')
# except ValueError:
#     print("You did not enter a base 10 number! Try again")

textToProcess = input("Enter text:  ")
r = requests.post('http://text-processing.com/api/sentiment/', data={"text":textToProcess})
print(type(r))
print(r)

try:
    label = r.json()['label']
    print(label)
except JSONDecodeError:
    print("We could not decode the JSON response!")
except KeyError:
    print("We got JSON back from the sentiment analysis, but it did not have a key 'label'")

raise APIThrottleLimitError
# # print(r)
