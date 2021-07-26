try:
    a=int(input("enter a"))
    b=int(input("enter b"))
    c=a/b
except ZeroDivisionError:
    print("Division by zero is not possible")
else:
    print(c)
#else is executed only when there is no exception
#no exception-else is executed
'''
enter a24
enter b12
2.0
'''
#exception-else is not executed
'''
enter a24
enter b0
Division by zero is not possible
'''

