#Input:My Cse A students Are Very active
#output:mY cSE a STUDENTS aRE vERY ACTIVE
str1='My Cse A students Are Very active'
str=''
for i in range(len(str1)):
    if str1[i].isupper():
        str=str+str1[i].lower()
    elif str1[i].islower():
        str=str+str1[i].upper()
    else:
        str=str+str1[i]
print(str)
