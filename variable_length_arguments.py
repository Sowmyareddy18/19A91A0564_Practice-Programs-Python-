#variable lenght arguments-*
def add_n(a,b):
    s=a+b
    return s
print(add_n(5,6))


def add_n(*a):
    s=0
    print(type(a))#<class 'tuple'>
    for i in a:
        s+=i
    return s
print(add_n(5,6))
print(add_n(5,6,7,4))


def add_n(b,c,*a):
    s=0
    for i in a:
        s+=i
    return s+b+c
print(add_n(5,6,7))
print(add_n(5,6,7,4))
'''
11
<class 'tuple'>
11
<class 'tuple'>
22
18
22
'''
