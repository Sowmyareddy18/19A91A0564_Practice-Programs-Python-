names=["CSEA","CSEB"]#List Creation with two elements
print(names)#['CSEA', 'CSEB']
names.append("CSEC")
names.insert(2,"IT")
print(names)#['CSEA', 'CSEB', 'IT', 'CSEC']
#Empty List
branches=[]
size=len(branches)#length of branches list
print("length of branchs %d"%(size))#Zero
#Add elements to the empty list
#append()-Append the elements to the end of list
branches.append("CSE")
branches.append("IT")
branches.append("CIVIL")
#printing
print(branches)#['CSE','IT','CIVIL']

#Another method to add elements at a particular index
#insert(index,object)
branches.insert(2,"Mech")
print(branches)#['CSE', 'IT', 'Mech', 'CIVIL']

#Slicing-extarcting certain elements from the list
print(branches[0:2])#Index 0 to end-1
print(branches[1:])#from index 1 to end
print(branches[:3])#from 0 to end-1
print("Negative Sclice Indexing")
print(branches[-2])
'''
['CSE', 'IT']
['IT', 'Mech', 'CIVIL']
['CSE', 'IT', 'Mech']
Negative Sclice Indexing
Mech
'''

