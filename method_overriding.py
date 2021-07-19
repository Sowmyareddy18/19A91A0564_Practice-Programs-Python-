'''
Overriding-Subclass overrides the behaviour of the super class methods
Declaring the method in the subclass with the same signature if super class except the impelmentation
'''
class Faculty:
    def show(self):
        print("from employee class")
class Subject(Faculty):
    def show(self):
        print("Subject class inherited from Faculty")
emp=Faculty()
emp.show()
sub=Subject()
sub.show()
'''
from employee class
Subject class inherited from Faculty
'''
