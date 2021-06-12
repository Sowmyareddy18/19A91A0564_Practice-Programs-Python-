n = int(input())
s = set(map(int, input().split()))
op=int(input())
for i in range(op) :
    choice=input().split()
    if choice[0]=="pop" :
        s.pop()
    elif choice[0]=="remove" :
        s.remove(int(choice[1]))
    elif choice[0]=="discard" :
        s.discard(int(choice[1]))
print (sum(s))
'''
INPUT:
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop
discard 6
remove 5
pop
discard 5
OUTPUT:
4
