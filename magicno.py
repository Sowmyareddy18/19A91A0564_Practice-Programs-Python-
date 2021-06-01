#n=45684
#if n%9==0:
#    print(9)
#else:
#   print(n%9)
n=int(input('enter a number'))
sum=n
while sum>9:
    n=sum
    sum=0
    while n>0:
        r=n%10
        sum=sum+r
        n=n//10
print(sum)


