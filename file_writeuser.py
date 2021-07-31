#Writing Program
fp=open("Student.txt","w")
for i in range(3):
    #name=input("enter your friends name")
    #fp.write(name)
    fp.write(input("Enter your friends name"))
    fp.write('\n')

fp.close()
fp=open("Student.txt","r")
str1=fp.read()
print("Data from Student.txt")
print(str1)
fp.close()
'''
Enter your friends namesarvani
Enter your friends namevyshnavi
Enter your friends namesharon
Data from Student.txt
sarvani
vyshnavi
sharon
'''
