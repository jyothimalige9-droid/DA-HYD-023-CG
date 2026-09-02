'''file handling in python--->files are used to store the data

it supports-->read,write,append using open()

#first lets understand how we can access .txt files using python

import os  #os module is used to access the files
if os.path.exists('sample.txt'):
    file =open('sample.txt','r')
    print("file is loaded successfully")
else:
    print("file is not present")

#now let us access the contentfrom the file



file=open('sample.txt','r')
#print(file)
#print(file.read())#reads the entire content from the file
#print(type(file.read()))
#print(len(file.read()))
#a=file.read()
##print(a)
#print(len(a))
print(file)
#print(file.readline())#reads single line from the file
print(file.readlines())

#'w' mode-->it automatically creates a new file.if the file is exist
#it overrides the content in it

file=open('data.txt','w')
print(file)
file.write("Good afternoon guys,how are you doing")
file.write("Today is wednesday")
file.close()

#we can also will keyword to avoid close()

with open('data.txt','w')as f:
    f.write("Now checking what happend")

#'a' --> it also automatically creates a file,but if the file is already
#existing it appends the content to the previous file

with open('data.txt','a')as g:
    g.write("\n okay let us see how its going")



with open('data.txt','r+')as h:
    print(h.read())
    h.write("today is wednesday")

with open('data.txt','r+')as h:
    h.write("today is wednesday")
    print(h.read())

#file operations size and path
import os
file=open('data.txt','r')
if os.path.exists(file):
    print("file size is",os.path.getsize(),"bytes")
    print("file absolute path is",os.path.abspath(file))
else:
    print("file is not present")'''

#if your project is requiring file handling use it....
#tokens --> operators -->control statement ,while,if,else,elif,break
#pop (functions/*args/**kwargs))-->oop
#data analytics --> Numpy,pandas,data visualisation
    




















    

































































    










































