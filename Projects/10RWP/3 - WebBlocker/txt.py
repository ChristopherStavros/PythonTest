with open('my_file.txt', 'r+') as f:
    content = f.read()
    print(content)
    f.write("Hello \n")
    
