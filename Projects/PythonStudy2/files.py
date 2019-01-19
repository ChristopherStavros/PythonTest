#Files must be closed in Python or Python may not finish writing to them

# Using the with construct, there is no need to close the file
with open('myfile.txt', 'w') as f:
    f.write('Hello world')

