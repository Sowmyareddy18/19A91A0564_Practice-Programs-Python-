try:
    a=int(input("enter a"))
    b=int(input("enter b"))
    c=int(input("enter c"))
    a=a/b#if b is zero then ZeroDivisionError
    print(a)
    print(res)#Exception Raised-NameError
except TypeError:
    print("Conversio problem")
except NameError:
    print("variable is not yet defined")
except ZeroDivisionError:
    print("Dont perform division with zero")
except:
    pass

'''
enter a10
enter b5
enter c2
2.0
variable is not yet defined
'''
'''
enter a24
enter b0
enter c6
Dont perform division with zero
'''
'''
enter a10
enter bxyz
'''
