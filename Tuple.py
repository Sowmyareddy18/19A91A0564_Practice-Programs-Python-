#tuple creation
b=("CSE","IT","Mech","ECE","CSE","AGRI","PT")
#print
print(b)
#Data type of b
print(type(b))
#size of tuple
print("Size of tuple is : {}".format(len(b)))#4
#max element
max_ele=max(b)
print("Max element is %s"%(max_ele))
min_ele=min(b)
print("Min element is %s"%(min_ele))
repetition=b.count("CSE")
print("CSE is repeated %s times"%(repetition))
#sclicing
print(b[1])#IT
print(b[2:5])#Mech,ECE,CSE #(start to endindex-1)
print(b[:5])#('CSE', 'IT', 'Mech', 'ECE', 'CSE')
print(b[3:])#('ECE', 'CSE', 'AGRI', 'PT')
print(b[:])#('CSE', 'IT', 'Mech', 'ECE', 'CSE', 'AGRI', 'PT')
#start to end with step count
print(b[::2])#('CSE', 'Mech', 'CSE', 'PT')
print(b[::3])#('CSE', 'ECE', 'PT')
print(b[1:5:2])#('IT', 'ECE')
#Negative indexing
print(b[::-2])#('PT', 'CSE', 'Mech', 'CSE')
print(b[::-3])#('PT', 'ECE', 'CSE')
print(b[::1])#All elements from left to right
print(b[::-1])#All elements form right to left(reverse)
print(b[-5:-2])#('Mech', 'ECE', 'CSE')
print(b[-2:-5])#()
#Methods
#1.count
#2.index
result=b.index("Mech")
print(result)#2
'''
('CSE', 'IT', 'Mech', 'ECE', 'CSE', 'AGRI', 'PT')
<class 'tuple'>
Size of tuple is : 7
Max element is PT
Min element is AGRI
CSE is repeated 2 times
IT
('Mech', 'ECE', 'CSE')
('CSE', 'IT', 'Mech', 'ECE', 'CSE')
('ECE', 'CSE', 'AGRI', 'PT')
('CSE', 'IT', 'Mech', 'ECE', 'CSE', 'AGRI', 'PT')
('CSE', 'Mech', 'CSE', 'PT')
('CSE', 'ECE', 'PT')
('IT', 'ECE')
('PT', 'CSE', 'Mech', 'CSE')
('PT', 'ECE', 'CSE')
('CSE', 'IT', 'Mech', 'ECE', 'CSE', 'AGRI', 'PT')
('PT', 'AGRI', 'CSE', 'ECE', 'Mech', 'IT', 'CSE')
('Mech', 'ECE', 'CSE')
()
2
'''
