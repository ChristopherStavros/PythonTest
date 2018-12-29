'''
Regular expression practice
'''
#non regex = find('T") returns first index where char is found..in this case index 1 
#print("STUFFTT".find('T'))

#REGEX
import re

#text to search
textToSearch = 'This is some text with some phone numbers such as 555-555-5555 and 554-554-5544 and (111)-111-1111'

#phone number regex pattern - re.compile() function - uses raw string and \d (digit)
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

#match object - this only returns the first occurrance of a phone number!
mo = phoneNumRegex.search(textToSearch)
#print(mo.group())

#INSTEAD - the findall fnction finds all occurrances of a phone number and returns a list of strings or a list of tuples of strings
#print(phoneNumRegex.findall(textToSearch))

#using groups
phoneNumRegex2 = re.compile(r'(\(\d\d\d\)|\d\d\d)-(\d\d\d-\d\d\d\d)')
#print(phoneNumRegex2.findall(textToSearch))

#returns ['his', ' is']...weird
anythingExceptNewline = re.compile(r'.is')
#print(anythingExceptNewline.findall(textToSearch))

#returns ['This', ' is']...notice that [ is] includes a white space
anythingExceptNewline = re.compile(r'.{1,2}is')
#print(anythingExceptNewline.findall(textToSearch))

#returns ['This is']
anythingExceptNewline = re.compile(r'.+is')
#print(anythingExceptNewline.findall(textToSearch))

#returns ['This is'] because the text starts with the pattern
anythingExceptNewline = re.compile(r'^.+is')
#print(anythingExceptNewline.findall(textToSearch))

#re.I or re.IGNORECASE
This = re.compile(r'this', re.IGNORECASE)
# print(This.findall(textToSearch))

textToSearch2 = "Agent Alice gave the secret documents to Agent Bob"
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall(textToSearch2))

#ONLY returns the group!!!!!
namesRegex = re.compile(r'Agent (\w)\w*')

#Agent A**** gave the secret documents to Agent B**** .......\1 means group1 or the first group found
print(namesRegex.findall(textToSearch2))
print(namesRegex.sub(r'Agent \1****', textToSearch2))

#\w is alpha nummeric...this returns ['Agent 1abc', 'Agent 2def'] 
textToSearch2 = "Agent 1abc gave the secret documents to Agent 2def"
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall(textToSearch2))