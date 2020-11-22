import math as m
N=int(input())
A=list(map(int,input().split()))

ans=0
m=0
for i in range(2,1001):
    mm=0
    for j in A:
        if j%i==0:
            mm+=1
    if m<mm:
        m=mm
        ans=i
print(ans)