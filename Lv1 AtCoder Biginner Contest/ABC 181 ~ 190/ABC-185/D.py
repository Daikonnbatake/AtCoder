import math as m
N,M=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
A.append(N)
A.insert(0,0)
a=[0]*(M)
for i in range(1,M+1):
    b=A[i]-A[i-1]-1
    if b!=0:a[i-1]=b
    else:a[i-1]=10**10
ans=0
s=min(a)
print(a,s)
for i in a:
    if 0<i:ans+=m.ceil(i/s)
print(ans)