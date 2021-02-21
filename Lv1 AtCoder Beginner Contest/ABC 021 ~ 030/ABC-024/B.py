N,T=map(int,input().split())
A=[int(input()) for i in range(N)]
ans=0
for i in range(1,N):
    if A[i-1]+T < A[i]: ans+=T
    else: ans+=A[i]-A[i-1]
print(ans+T)