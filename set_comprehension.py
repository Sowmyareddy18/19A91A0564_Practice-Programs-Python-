#set comprehension
L1=[2,4,8,8,16,17,17]#created list of values
print("List comprehension")
L2=[i*2 for i in L1]
print(L2)#[4, 8, 16, 16, 32, 34, 34]
L3={i*2 for i in L1}##from the list created a new set of unique values
print("set comprehension")
print(L3)#{32, 34, 4, 8, 16}
