'''
6.3
Sort the two lists
L1=[45,63,23,12,78]
L2=[12,90,72,-1]
Combine L1&L2 as single list and display the elements in the sorted order
#Dislay
L3=[-1,12,12,23,45,63,72,78,90]
Perform sorting on the list.....
'''
l1=[]
l2=[]
n1=int(input("enter how many values in list 1"))
for i in range(n1):
    number=int(input())
    l1.append(number)
n2=int(input("enter how many values in list 2"))
for i in range(n2):
    number=int(input())
    l2.append(number)
l3=l1+l2
l3.sort()
print(l3)
'''
OUTPUT:
enter how many values in list 1 4
12 
23
45
56
enter how many values in list 24
34
56
67
45
[12, 23, 34, 45, 45, 56, 56, 67]
'''
