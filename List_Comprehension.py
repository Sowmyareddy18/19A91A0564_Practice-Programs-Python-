#Comprehension-List
'''
without listcomprehension
Create an empty list and add even numbers in the list
The range of even numbers is 1 to 10
'''
L1_even=[]
for i in range(1,11):
    #even number verification
    if i%2==0:
        #Add number to even list
        L1_even.append(i)
#print the list
print("Even list")
print(L1_even)#[2, 4, 6, 8, 10]
'''
List Comprehension
Syntax:
res_list=[expression/outputvariable for in iterableobject filter/ifcondition]
'''
res_list=[i for i in range(1,11)]
print("List Comprehension")
print(res_list)#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res_listeven=[i for i in range(1,11) if i%2==0]
print("Even list")
print(res_listeven)#[2, 4, 6, 8, 10]
'''
first i value is fetched and check the condition,
if the condition is true then i is returned to the expression  
'''
res_listeven=[i for i in range(1,21) if i%2==0]
print(res_listeven)#[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
res_list=[1 if i==0 else 2*i for i in range(0,11)]
print(res_list)#[1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
'''
output:
Even list
[2, 4, 6, 8, 10]
List Comprehension
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even list
[2, 4, 6, 8, 10]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
[1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
'''
