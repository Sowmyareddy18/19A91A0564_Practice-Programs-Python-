import os
fp=open("demo.txt","r")
data=fp.read()
print("content of the file:",data)
size=os.path.getsize("demo.txt")
print("The size of the file demo.txt is ",size)
occurrences=data.count("CSE")
print("Number of occurrences of CSE in demo.txt file:",occurrences)
fp.close()
'''
content of the file: Hello CSE
I am from CSE
Roll number 19A91A0564
The size of the file demo.txt is  48
Number of occurrences of CSE in demo.txt file: 2
'''
