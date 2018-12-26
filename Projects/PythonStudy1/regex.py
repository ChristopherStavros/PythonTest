'''
Regular expression practice
'''
import re

#text to search
textToSearch = 'This is some text with some phone numbers such as 555-555-5555 and 554-554-5544 and (111)-111-1111'

#phone number regex pattern - re.compile() function - uses raw string and \d (digit)
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

#match object - this only seems to return the first occurrance of a phone number!
mo = phoneNumRegex.search(textToSearch)
print(mo.group())

#INSTEAD - the findall fnction finds all occurrances of a phone number and returns a list
print(phoneNumRegex.findall(textToSearch))

#using groups
phoneNumRegex2 = re.compile(r'(\(\d\d\d\)|\d\d\d)-(\d\d\d-\d\d\d\d)')
print(phoneNumRegex2.findall(textToSearch))