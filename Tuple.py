#tuple creation
bra=("CSE","IT","Mech","ECE","CSE")
#print
print(bra)
#Data type of bra
print(type(bra))
#size of tuple
print("Size of tuple is : {}".format(len(bra)))#4
#max element
max_ele=max(bra)
print("Max element is %s"%(max_ele))
min_ele=min(bra)
print("Min element is %s"%(min_ele))
repetition=bra.count("CSE")
print("CSE is repeated %s times"%(repetition))

'''
OUTPUT:
('CSE', 'IT', 'Mech', 'ECE', 'CSE')
<class 'tuple'>
Size of tuple is : 5
Max element is Mech
Min element is CSE
CSE is repeated 2 times
'''
