class student:
    collegename="AEC"#class Attribute
    #instance attribute-class function
    def __init__(self):
        self.section="B"#instance attribute
s1=student()
s1.section="A"
print(s1.section)#A
print(s1.collegename)#AEC
s2=student()
print(s2.section)#B
print(s2.collegename)#AEC
