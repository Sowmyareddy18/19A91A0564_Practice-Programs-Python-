branch_names=["CSE","IT","ECE","MECH","AGRI"]
print(branch_names)
print(branch_names[1])
print(branch_names[4])
print("Data Type of branch_name",type(branch_names))
colleges=["AEC","JNTUK","IIT",2,3,"KKD",8.8,"SURAMPALEM"]
print(colleges)
print("Data Type of College is",type(colleges))
#modifing list
branch_names[3]="PT"
print(branch_names)#['CSE', 'IT', 'ECE', 'PT', 'AGRI'] 
for i in branch_names:
    print(i,end=" ")#print(*object,sep,end)

#output:
'''
['CSE', 'IT', 'ECE', 'MECH', 'AGRI']
IT
AGRI
Data Type of branch_name <class 'list'>
['AEC', 'JNTUK', 'IIT', 2, 3, 'KKD', 8.8, 'SURAMPALEM']
Data Type of College is <class 'list'>
['CSE', 'IT', 'ECE', 'PT', 'AGRI']
CSE IT ECE PT AGRI
'''
#print elements in list with out for loop
a=[1,2,3,4,5]
print(*a,sep="**",end=" ")#1**2**3**4**5
#size of  List
a=[10,20,30,40,50]
n=len(a)
print(n)
for i in range(n):
    print(a[i])
'''
5
10
20
30
40
50
'''
#slicing of list
print(a[2:])
#[30, 40, 50]
