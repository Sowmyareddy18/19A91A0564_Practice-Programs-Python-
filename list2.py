#List-Construction-list()
L1=list((10,20,30,40,50))#L1 is created
L2=list((60,70,80,90,100))#L2 is created
print(*L1)#element by element without loop
'''
for i in L1:
   print i,
'''
#functions
#print("Comparing L1 with L1 is %d" %cmp(L1,L1))#0
print("Minimum element from List 1 is %d"%min(L1))#10
print("Maximum element from List 2 is %d"%max(L2))#100
#list(string)-converts the given string/turple into list object
s="hello"
z=list(s)
print(z)#['h', 'e', 'l', 'l', 'o']
#methods
b=list(("Banana","Kiwi"))#constructor
print(b)
b.append("Jiwi")#listobject.append(value)
for i in b:
    print(i)
'''
['Banana', 'Kiwi']
Banana
Kiwi
Jiwi
'''
