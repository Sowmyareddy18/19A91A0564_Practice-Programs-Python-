#Definition of functon
def test():
    print("test()")
    print("I am function")
    print("Hello")
#call function
test()#function call
'''
test()
I am function
Hello
'''
#function with parameter
def show(x):
    print("show()")
    print(x)
    print(type(x))
#call the show()
show("Python")#show() with string value
show(10)#show() with integer value
show(23.45667)#show() wiht float value
set1={1,2,3,4,5,6}
show(set1)#show() with set DS
list1=["pyhton","FLAT","CO","DAA","IOT"]
show(list1)#show() with list DS
dict1={5:"CSE",12:"IT",3:"ECE"}
show(dict1)#show() with dictionary DS
tuple1=(10.4,10.5,213.34)
show(tuple1)#show() with tuple DS
'''
show()
Python
<class 'str'>
show()
10
<class 'int'>
show()
23.45667
<class 'float'>
show()
{1, 2, 3, 4, 5, 6}
<class 'set'>
show()
['pyhton', 'FLAT', 'CO', 'DAA', 'IOT']
<class 'list'>
show()
{5: 'CSE', 12: 'IT', 3: 'ECE'}
<class 'dict'>
show()
(10.4, 10.5, 213.34)
<class 'tuple'>
'''
