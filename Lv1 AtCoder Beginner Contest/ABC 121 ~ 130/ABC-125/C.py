import math
N=int(input())
A=tuple(map(int,input().split()))
L,R=0,[0]*N
R[-1]=A[-1]
ans=0

for i in range(1,N):
    i=N-i
    R[i-1] = math.gcd(A[i-1],R[i])

for i in range(N):
    if i==0:
        ans=max(ans, R[1])
    elif i==N-1:
        ans=max(ans,L)
    else:
        ans=max(ans,math.gcd(L,R[i+1]))
    L=math.gcd(L,A[i])

print(ans)