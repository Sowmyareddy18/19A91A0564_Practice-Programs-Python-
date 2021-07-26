#open the file
fp=open("ABCDE.java","r")
#perform the read operation
str1=fp.read(5)
print("five bytes of data from ABCDE.java file")
print(str1)
str2=fp.read(15)
print("next 15 bytes of data from ABCDE.java file")
print(str2)
str3=fp.read()
print("Remaining Data")
print(str3)
'''five bytes of data from ABCDE.java file
class
next 15 bytes of data from ABCDE.java file

{
public
Remai
Remaining Data
ning Data
static void main(String args[])
{
System.out.println('j'+'a'+'v'+'a');
}
}
'''
