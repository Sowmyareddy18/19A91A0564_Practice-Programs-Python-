class Faculty:
    def __init__(self,n,s):
        self.name=n
        self.subject=s
    def print_details(self):
        print("Name :",self.name)
        print("Subject :",self.subject)
obj1=Faculty("Devi priya","Python")
obj1.print_details()
obj2=Faculty("Govindaraju","FLAT")
obj2.print_details()
name=input("enter name")
sub=input("enter subject")
obj3=Faculty(name,sub)
obj3.print_details()
'''
Name : Devi priya
Subject : Python
Name : Govindaraju
Subject : FLAT
enter nameKumar
enter subjectCO
Name : Kumar
Subject : CO
'''

        
