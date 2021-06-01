str1='I am CSE A'
str2=' Hai'
str3=str1+str2
print(str3)
length_str1=len(str1)
print('length of str1',length_str1)
print('length of str2',len(str2))
print('character at index 2',str1[2])
print('sub string',str1[2:6])
result="csea"*5;
print(result)
print(str1.split(" "))#default seperator is space
print(str1.split(" ",2))
s='Hello CSE-A Hello'
s1='CSE-A'
print('count function')
print(s.count('hello'))#0
print(s.count(s1))#1
#Replacing String
#object.replace('old','new')
s='Hello World'
result=s.replace('Hello','Good')
print(result)
print(s)
#Good World
#Hello World-original string
#Finding string
print('Find')
Mainstring='Python Programming Python'
result=Mainstring.find('Python')
print(result)#0
result=Mainstring.find('Sleeping...CSEA')
print(result)#-1
#comparition
print('Hello'=='Hello')
print('Hello'=='hello')
#True
#False
