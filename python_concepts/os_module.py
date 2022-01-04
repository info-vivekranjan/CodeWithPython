import os

path = '/home/vivek/Documents/menuItem.txt'

if os.path.exists(path):
    print('This path exits')
    if os.path.isfile(path):
        print('This is a file')
    else:
        print('This is not a file')
else:
    print('Path does not exist')


# Reading a file 

try:
    with open(path) as file:
        print(file.read())
except FileNotFoundError:
    print('File not found in that directory')       
except Exception as e:
    print(e)


# Writing a file
content = "This is the file you want to write, \n After that we are appending"

with open('test.txt','a') as file:
    file.write(content)

# Copying a file

import shutil
shutil.copyfile('test.txt', 'copied.txt')

# Moving a file

os.replace(path, 'copied.txt')

# Deleteing  A File

os.remove('/home/vivek/Videos/CodeWithPython/python_concepts/test2.txt')