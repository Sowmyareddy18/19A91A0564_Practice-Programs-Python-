a = set(map(int,input().split()))
count=0
n=int(input())
for i in range(n):
    b = set(map(int,input().split()))
    if a.issuperset(b):
        count+=1
if count==n:
    print(True)
else:
    print(False)
'''
INPUT:
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12
OUTPUT:
False
'''
