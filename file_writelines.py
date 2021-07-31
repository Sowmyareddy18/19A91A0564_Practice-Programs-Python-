fp=open("Friends.txt","w")
mylist=['vidhya\n','vandana\n','hema\n']
fp.writelines(mylist)
print("Data Saved.........")
fp.close()
print(mylist)
'''
Data Saved.........
['vidhya\n', 'vandana\n', 'hema\n']
'''
