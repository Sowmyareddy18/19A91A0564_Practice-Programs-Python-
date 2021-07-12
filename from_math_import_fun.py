#from modulename import function name/variablename
from math import floor,ceil,pi
number=12.4
res=floor(number)
print(res)
res=ceil(number)
print(res)
print(pi)#constant value in math module
res=cos(1)#NameError: name 'cos' is not defined
print(res)

'''
12
13
3.141592653589793
Traceback (most recent call last):
  File "F:/19A91A0564/from_math_import_fun.py", line 9, in <module>
    res=cos(1)
NameError: name 'cos' is not defined
'''
