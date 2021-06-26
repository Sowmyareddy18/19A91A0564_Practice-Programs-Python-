def factorial(number):
      fact=1
      for i in range(1,number+1):
            fact=fact*i
      print("fact %d is %d" %(s,fact))
def printS():
      print("Gloabal variable s is %d" %s)#print gloabal varaible s
s=int(input("Enter number"))#s scope is started from this statement
factorial(s)
printS()
'''
Enter number7
fact 7 is 5040
Gloabal variable s is 7
'''
