#local variable-global variable
s=int(input("Enter the number"))#global variable
def factorial(number):
    fact=1#local variable and scope is limited to factorial fun only
    for i in range(1,number+1):
        fact=fact*i
    print("Fact of %d is %d"%(s,fact))#global variable used in factorial function
#call function
factorial(s)
print("Fact is %d"%fact)#NameError: name 'fact' is not defined-access-out side of the fun
'''
Enter the number7
Fact of 7 is 5040
'''
