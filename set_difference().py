n = input()
a = set(map(int, input().split()))
n = input()
b = set(map(int, input().split()))
print(len(a.difference(b)))
'''
INPUT:
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
OUTPUT:
4
'''
