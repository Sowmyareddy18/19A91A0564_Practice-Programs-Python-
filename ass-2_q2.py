fp=open("demo.txt","r")
data=fp.read()
upper=0
lower=0
digit=0
for letter in data:
    if letter.isupper():
        upper+=1
    if letter.islower():
        lower+=1
    if letter.isdigit():
        digit+=1
fp.close()
print("Number of upper case letters :",upper)
print("Number of lower case letters :",lower)
print("Number of digits:",digit)
'''
Number of upper case letters : 11
Number of lower case letters : 19
Number of digits: 8
'''
