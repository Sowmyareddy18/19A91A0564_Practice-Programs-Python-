n = input()
a = set(map(int, input().split()))
n = input()
b = set(map(int, input().split()))
set1=sorted(a.symmetric_difference(b))
for i in (set1):
    print(i)
'''
INPUT:
4
2 4 5 9
4
2 4 11 12
OUTPUT:
5
9
11
12
'''
