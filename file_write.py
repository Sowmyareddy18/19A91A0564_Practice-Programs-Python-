#Writing program
fp=open("Student.txt","w")#if file is not existed earlier,it will be created
fp.write("I am from CSE-A")#write content
fp.close()
fp=open("Student.txt","r")
str1=fp.read()
print("Data from Student.txt")
print(str1)
fp.close()
'''
Data from Student.txt
I am from CSE-A
'''
