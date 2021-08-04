fp=open("GamesRecord.txt","w")
r=["Sno \t","Name\t","Game\n"]
fp.writelines(r)
n=int(input("Enter number of rows"))
for i in range(n):
    fp.writelines([input(),"\t",input(),"\t",input()])
    fp.write("\n")
fp.close()
fp1=open("GamesRecord.txt","r")
data=fp1.read()
print(data)
fp1.close()
'''
Enter number of rows3
1
Rahul
cricket
2
David
chess
3
Ram
vollyball
Sno 	Name	Game
1	Rahul	cricket
2	David	chess
3	Ram	vollyball
'''
