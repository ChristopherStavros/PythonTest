'''
advancedStrings.py

'''

#multiline string
multilineString ='''Hello
this is a
multiline string'''

print(multilineString)

spam = """Christopher's new "string" with 'triple quotes'"""
print(spam)
spam = r"Christopher's new 'raw string'. I had to be alot more careful about which types of quotes I was using in comparison to when I used 'triple quotes'"
print(spam)
spam

print("STring".isupper())
print("STring".islower())
print("STring".upper().isupper())
print("STring".lower().islower())

var = "hello"
print(var.upper())