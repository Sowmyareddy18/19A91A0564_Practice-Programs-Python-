class Employee:
    def __init__(self,identification,name):
        self.id=identification
        self.name=name
    def show(self):
        print("hello",self.name)
        print("id is",self.id)
class Faculty(Employee):#Subclass that acquires the properties of super class
    def subjectoffered(self):
        print("python & java")
class Admin(Employee):
    def checkSeatingArrangement(self):
        print("Seats arrangement is confirmed")
f=Faculty(334,"Priya")
f.show()
f.subjectoffered()
a=Admin(208,"Rohit")
a.show()
a.checkSeatingArrangement()
'''
hello Priya
id is 334
python & java
hello Rohit
id is 208
Seats arrangement is confirmed
'''
