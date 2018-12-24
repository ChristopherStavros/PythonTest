import os

for item in os.listdir("c:\\_Repositories"):
    print(item)

for item in os.walk("c:\\_Repositories"):
    for i in item:
        print(i)