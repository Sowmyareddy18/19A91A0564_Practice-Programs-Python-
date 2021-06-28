#keyword argument-**
#def fun(n1,n2,n3,*variable_len_args,**keyword_args)
def myfun(**kargs):
    print(type(kargs))
    for key,value in kargs.items():
        print(key,value)
myfun(name="sowmya",subject="maths")
'''
<class 'dict'>
name sowmya
subject maths
'''
def add_n(b,c,*a,**key):
    s=0
    for i in a:
        s+=i
    for k,v in key.items():
        print(k,v)
    return s+b+c
print(add_n(5,6,7,8,name="xyz"))
'''
name xyz
26
'''
