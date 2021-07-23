try:
    a=int(input("enter a"))
    b=int(input("enter b"))
    c=a/b
    print(c)
except ZeroDivisionError:
    print("can't divide with zero")
print("I am Normal statement after exception handling")
'''
enter a24
enter b0
can't divide with zero
I am Normal statement after exception handling
'''
