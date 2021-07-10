#importing module
import random

#Accessing functions in random module

#random()-returns a random float number between 0.0 to 1.0
print(random.random())#0.704681155679289

#randint()- returns a random integer betwrrn the specified integers
print(random.randint(24,56))#46

#randrange()-returns a randomly selectes element from the range created by start,stop and step arguments
# by default the value of start is 0,the value if step is 1 
print(random.randrange(1,10,2))#5

#choice()-returns a randomly selected element from a non-empty sequence
print(random.choice([10,25,34,78,55,64]))#64

#print(random.choice())#empty sequence as argument raises an TypeError
#TypeError: choice() missing 1 required positional argument: 'seq'

#shuffle()-randomly reorders the elements in a list
list1=[20,15,30,46,37,51]
random.shuffle(list1)
print(list1)#[51, 46, 20, 37, 15, 30]

'''
0.704681155679289
46
5
64
[51, 46, 20, 37, 15, 30]
'''
