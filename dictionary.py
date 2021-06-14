#Dictionary to store branchcode->name
dict_ds={5:"CSE",12:"IT",3:"ECE",4:"MECH"}
print(dict_ds)#{5: 'CSE', 12: 'IT', 3: 'ECE', 4: 'MECH'}
#type of data structure
print(type(dict_ds))#<class 'dict'>
#accessing elements from the dictionary
res=dict_ds[12]#dictionary_name[key]
print("At key 12 the value is {}".format(res))#At key 12 the value is IT
dict_ds1={5:"CSE",5:"CSE-C","Name":"priya","Fname":"priya"}
#key-Unique,value-Repeated
print(dict_ds1)#{5: 'CSE-C', 'Name': 'priya', 'Fname': 'priya'}
#Modify the values from the dictionary
print("old value is %s"%dict_ds1["Name"])#dictionary_name[key]
dict_ds1["Name"]="Devi"#dictionary_name[key]=value
print("New value is %s"%dict_ds1["Name"])#Devi
#old value is priya
#New value is Devi
#dict_ds1[key]=value
dict_ds1["Department"]="CSE"
print("New Dict After adding Key")
print(dict_ds1)#{5: 'CSE-C', 'Name': 'Devi', 'Fname': 'priya', 'Department': 'CSE'}
'''
OUTPUT:
{5: 'CSE', 12: 'IT', 3: 'ECE', 4: 'MECH'}
<class 'dict'>
At key 12 the value is IT
{5: 'CSE-C', 'Name': 'priya', 'Fname': 'priya'}
old value is priya
New value is Devi
New Dict After adding Key
{5: 'CSE-C', 'Name': 'Devi', 'Fname': 'priya', 'Department': 'CSE'}
'''
