import math
def agcd(l):
    a=math.gcd(l[0],l[1])
    for i in range(2,len(l)):
        a=math.gcd(a,l[i])
    return a

N=int(input())
a=list(map(int,input().split()))
print(agcd(a) if 1<N else a[0])