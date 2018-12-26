'''
immutable.py

'''

spam = [1,2,3,4,5]
eggs = spam
eggs[0] = 'Hello'
print(eggs)
print(spam)

spam1 = [1,2,3,4,5,6]
eggs1 = spam1[:]
eggs1[0] = 'yoyoyo'

print(eggs1)
print(spam1)

def change(value):
    value = value[:]
    value.append('yoy')
    return value

new = change(spam1)

print(spam1)
print(new)