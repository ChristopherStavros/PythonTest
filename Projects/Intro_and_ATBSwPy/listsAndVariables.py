name = "Chris"
sentence = "My name is {}".format(name)
addition = " and I work for SteezCorp"
print(sentence)
print(sentence.upper())
print(sentence.lower())
print(sentence.replace("Chris", "Steez"))
print(sentence[-5:])
print(sentence[2:])
print(len(sentence))
print(sentence + addition)
print(len(sentence + addition))

newList = []

newList.append("I")
newList.append("do not like")
newList.append("my job")
newList.append("BIGLY")
newList.append("SAD!")

print(newList[1])

for l in newList:
    print(l)

newList.pop()
for l in newList:
    print(l)

newList.reverse()
for l in newList:
    print(l)






