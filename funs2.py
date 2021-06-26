#functoin with default values
def test(name="AEC",Rollno='501'):
    print("Hello "+name,Rollno)
#Read name from the user
input_name=input("Enter Branch Name")
#call function
test(input_name,"502")
#call function
test("CSE-A")
#call function
test()#call function without any parameters
'''
Enter Branch NameIT
Hello IT 502
Hello CSE-A 501
Hello AEC 501
'''
#order function
def display(name,age):
    print("Name is ",name)
    print("Age is ",age)
#call the display function
display("Ravi",20)
display("Raj",21)
#call the display function
display(21,"Rahul")
'''
Name is  Ravi
Age is  20
Name is  Raj
Age is  21
Name is  22
Age is  Rahul
'''
display(age=21,name="Rahul")
display(name="Raghu",age=20)
'''
Name is  Rahul
Age is  21
Name is  Raghu
Age is  20
'''
