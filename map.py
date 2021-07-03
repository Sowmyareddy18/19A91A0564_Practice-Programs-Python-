#lambda-Map
#map(function_name,sequence,[sequence]..)
l1=[1,2,3,4]
l2=[5,6,7,8]
res=map(lambda a,b:a+b,l1,l2)
print(list(res))#[6, 8, 10, 12]

def fun(letter):
    char=['a','e','i','o','u']
    if letter in char :
        return True
    else:
        return False
data=['s','o','w','m','y','a']
res=map(fun,data)
print(list(res))


res=map(lambda letter:letter in ['a','e','i','o','u'],['s','o','w','m','y','a'])
print(list(res))

'''
[False, True, False, False, False, True]
[False, True, False, False, False, True]
'''

