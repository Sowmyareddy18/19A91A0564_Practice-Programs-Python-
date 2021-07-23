#Exception handling
try:
    print(x)  #Generates Exception
except NameError:
    print("x variable is not yet declared")
print("I am Normal statement after exception handling")

'''
x variable is not yet declared
I am Normal statement after exception handling
'''
