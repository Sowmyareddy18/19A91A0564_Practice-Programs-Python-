#Function with return expression
def greetings():
    print("Hi")
    return "Good AfterNoon CSE-A"
#call the greetings() and catch the value returned by greetings()
#variable=function_name()
result=greetings()
print(result)
print("second way of calling")
print(greetings())
'''
Hi
Good AfterNoon CSE-A
second way of calling
Hi
Good AfterNoon CSE-A
'''

#Create add() with three parameters and compute the addition and return result
def add(a,b,c):
    sum=a+b+c
    return sum
result=add(2,5,8)
print(result)#15
