import math as m
 
N=int(input())
A=list(map(int,input().split()))
 
l,r=[0]*(N+1),[0]*(N+1)
l[0],r[-1]=A[0],A[-1]
ans=1
 
for i in range(1,N+1):l[i]=m.gcd(l[i-1],A[i-1])
for i in range(1,N+1):r[N-i]=m.gcd(r[N-i+1],A[N-i])
l,r=l[1:],r[:-1]
 
for i in range(N):
    if i==0:a=r[1]
    elif i==N-1:a=l[-2]
    else:a=m.gcd(l[i-1],r[i+1])
    ans=max(ans,a)
    
print(ans)