#filter(function,iterable)
def function_filter_even(a):#list of values
    if a%2==0:
        return True
    else:
        return False
data=[1,2,3,4,5,6,7]
res=filter(function_filter_even,data)
print(list(res))#[2, 4, 6]

#lambda-filter

res=filter(lambda a:a%2==0,[1,2,3,4,5,6])
print(list(res))#[2, 4, 6]

#Dont have function to perform test
res=filter(None,[1,2,3,4,5,6])
print(list(res))#[1, 2, 3, 4, 5, 6]
'''
[2, 4, 6]
[2, 4, 6]
[1, 2, 3, 4, 5, 6]
'''
