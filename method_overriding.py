'''
Overriding-Subclass overrides the behaviour of the super class methods
Declaring the method in the subclass with the same signature of super class except the impelmentation
'''
class Faculty:
    def show(self):
        print("from Faculty class")
class Subject(Faculty):
    def show(self):
        print("Subject class inherited from Faculty")
f=Faculty()
f.show()
sub=Subject()
sub.show()
'''
from Faculty class
Subject class inherited from Faculty
'''
