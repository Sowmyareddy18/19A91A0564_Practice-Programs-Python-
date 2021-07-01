res=lambda x:x%2>0
print(res(19))#True
print(res(200))#False



res_large=lambda a,b:a>b
a=int(input("enter number1"))
b=int(input("enter number2"))
print(res_large(a,b))
if res_large(a,b):
    print("a is large")
else:
    print("b is large")
'''
True
False
enter number120
enter number245
False
b is large
'''
