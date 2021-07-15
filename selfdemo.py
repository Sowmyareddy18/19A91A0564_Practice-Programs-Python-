class Student:
    def read_details(self,section,name):
        s=section
        n=name
        print(s)#A
        print(n)#sowmya
a=Student()
a.read_details("A","sowmya")
#implicitly
#read_details(object,"A","sowmya")

'''
Traceback (most recent call last):
  File "F:/19A91A0564/selfdemo.py", line 11, in <module>
    a.read_details("A","sowmya")
TypeError: read_details() takes 2 positional arguments but 3 were given
'''
