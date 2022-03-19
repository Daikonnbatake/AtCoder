N,M=map(int,input().split())
a=[0]*(N+1)
for i in range(M):a[int(input())]=1

if N==1:
    print(1)
    exit()


mod=10**9+7
dp=[0]*(N+1)
dp[1]=0 if a[1] else 1

if a[1]: dp[2]=0 if a[2] else 1
else:dp[2]=0 if a[2] else 2

for i in range(3,N+1):
    if a[i]:continue
    if i==1:A,B=0,0
    else:A,B=dp[i-1],dp[i-2]
    dp[i]=(A+B)%mod

print(dp[-1])