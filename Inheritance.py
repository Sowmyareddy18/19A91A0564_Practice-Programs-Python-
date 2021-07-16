class Shape:
    def access(self):
        print("Hello from super class")
class Rectangle(Shape):
    def access_rect(self):
        print("I am from sub class")
r=Rectangle()#created object for sub class
r.access_rect()
r.access()
'''
I am from sub class
Hello from super class
'''
