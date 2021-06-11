x={1,2,3}
x.add(123456)
print('Mutable set',x)#Mutable set {123456, 1, 2, 3}
print(x.pop())#123456
#create a set as a IMMUTABLE-Frozen
y={678,890,788,567}
y=frozenset(y)#normal set is converted to frozenset
z=frozenset({132,245,567,345})
print(type(x))#<class 'set'>
print(type(y))#<class 'frozenset'>
print(y)
y.add(345) #AttributeError: 'frozenset' object has no attribute 'add'
res=y.union(z)
print("union",res)#union frozenset({132, 678, 788, 245, 567, 345, 890})
