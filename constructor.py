class A:
    def __init__(self,n):#Initialize the values to instance variables
        self.name=n
    def printdetails(self):
        print("hello",self.name)
o=A("sowmya")
o.printdetails()#hello sowmya
