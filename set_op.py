#Set operations
set1={1,2,3,4,5,10,12,13}
set2={10,11,12,13,14,15,17,19,1}
#union-All the elements-returns the union result as a new set
set3=set1.union(set2)
print("Union-set3",set3)#{1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 17, 19}
#Update
set1.update(set2)
print("Update-set1",set1)#{1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 17, 19}
set1={1,2,3,4,5,10,12,13}
set2={10,11,12,13,14,15,17,19,1}
set3=set1.intersection(set2)
print(set3)#{1, 10, 12, 13}
result=set2.intersection_update(set1)#result is available in the set4
print(set2)#{1, 10, 12, 13}
s1={1,2,3,4,5,10,12,13}
s2={10,11,12,13,14,15,17,19,1}
s3=s1.difference(s2)
print(s3)#{2, 3, 4, 5}
s1.difference_update(s2)
print(s1)#{2, 3, 4, 5}
a={1,2,3,4}
b={1,2,3,4,5,6,7,8}
print(a.issubset(b))#True(set a is subset od set b)
print(b.issubset(a))#False(set b is not subset of set a)
print(b.issuperset(a))#True(set b is super set of set a)
print(a.issuperset(b))#False(set a is not super set of set b)
'''
OUTPUT:
Union-set3 {1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 17, 19}
Update-set1 {1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 17, 19}
{1, 10, 12, 13}
{1, 10, 12, 13}
{2, 3, 4, 5}
{2, 3, 4, 5}
True
False
True
False
'''
