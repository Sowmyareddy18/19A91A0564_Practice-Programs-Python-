try:
    a=int(input("enter a"))
    b=int(input("enter b"))
    c=a/b
except ZeroDivisionError:
    print("Division by zero is not possible")
else:
    print(c)
finally:
    print("I am always executed")
#finally-must be executed\
#no exception
'''
enter a24
enter b12
2.0
I am always executed
'''
#exception
'''
enter a24
enter b0
Division by zero is not possible
I am always executed
'''
